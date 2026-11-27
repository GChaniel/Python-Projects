from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Accounts, Transaction


class AccountBalanceTests(TestCase):
    # Django creates these records in a separate test database.
    @classmethod
    def setUpTestData(cls):
        cls.account = Accounts.Accounts.create(
            first_name='Test', last_name='Account', initial_deposit=Decimal('100.00')
        )
        cls.other_account = Accounts.Accounts.create(
            first_name='Other', last_name='Account', initial_deposit=Decimal('50.00')
        )

    def test_home_lists_accounts(self):
        response = self.client.get(reverse('index'))

        self.assertContains(response, '<select name="account"')
        self.assertContains(response, 'Test Account')
        self.assertContains(response, 'Other Account')

    def test_account_selection_redirects_without_creating_a_transaction(self):
        response = self.client.post(reverse('index'), {'account': self.account.pk})

        self.assertRedirects(response, reverse('balance', kwargs={'pk': self.account.pk}))
        self.assertEqual(Transaction.TransactionDetails.count(), 0)

    def test_invalid_account_selection_shows_an_error(self):
        for value in ('', 'not-an-id', str(self.other_account.pk + 1000)):
            with self.subTest(value=value):
                response = self.client.post(reverse('index'), {'account': value})

                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.context['form'].errors['account'])

    def test_balance_without_transactions_shows_the_opening_deposit(self):
        response = self.client.get(reverse('balance', kwargs={'pk': self.account.pk}))

        self.assertEqual(response.context['balance'], Decimal('100.00'))
        self.assertContains(response, 'value="Test Account"')
        self.assertContains(response, 'value="100.00"')
        self.assertContains(response, 'No transactions yet.')

    def test_balance_uses_only_selected_accounts_transactions_in_date_order(self):
        # Create a later withdrawal first to check that dates determine the running balance.
        withdrawal = Transaction.TransactionDetails.create(
            account=self.account, date=date(2026, 11, 27), type='Withdraw',
            amount=Decimal('20.10'), description='Groceries'
        )
        deposit = Transaction.TransactionDetails.create(
            account=self.account, date=date(2026, 11, 26), type='Deposit',
            amount=Decimal('50.25'), description='Refund'
        )
        same_day_deposit = Transaction.TransactionDetails.create(
            account=self.account, date=date(2026, 11, 27), type='Deposit',
            amount=Decimal('1.00'), description='Adjustment'
        )
        Transaction.TransactionDetails.create(
            account=self.other_account, date=date(2026, 11, 26), type='Deposit',
            amount=Decimal('999.00'), description='Other account transaction'
        )

        response = self.client.get(reverse('balance', kwargs={'pk': self.account.pk}))

        self.assertEqual(response.context['balance'], Decimal('131.15'))
        self.assertEqual(list(response.context['table_contents'].items()), [
            (deposit, Decimal('150.25')),
            (withdrawal, Decimal('130.15')),
            (same_day_deposit, Decimal('131.15')),
        ])
        self.assertContains(response, 'Refund')
        self.assertContains(response, 'Groceries')
        self.assertNotContains(response, 'Other account transaction')

    def test_missing_account_returns_404(self):
        response = self.client.get(
            reverse('balance', kwargs={'pk': self.other_account.pk + 1000})
        )

        self.assertEqual(response.status_code, 404)

    def test_new_transaction_redirects_to_its_accounts_updated_balance(self):
        # Use the second account to check the redirect follows the submitted selection.
        response = self.client.post(reverse('transaction'), {
            'date': '2026-11-27',
            'type': 'Deposit',
            'amount': '25.50',
            'description': 'New deposit',
            'account': self.other_account.pk,
        }, follow=True)

        self.assertRedirects(response, reverse('balance', kwargs={'pk': self.other_account.pk}))
        self.assertEqual(response.context['account'], self.other_account)
        self.assertEqual(response.context['balance'], Decimal('75.50'))
        self.assertContains(response, 'New deposit')
        self.assertEqual(Transaction.TransactionDetails.count(), 1)

        # Following the redirect again is a GET and must not save a duplicate.
        self.client.get(reverse('balance', kwargs={'pk': self.other_account.pk}))
        self.assertEqual(Transaction.TransactionDetails.count(), 1)

    def test_invalid_transaction_stays_on_the_form_without_saving(self):
        response = self.client.post(reverse('transaction'), {
            'date': '2026-11-27',
            'type': 'Deposit',
            'amount': 'not-a-number',
            'description': 'Invalid deposit',
            'account': self.account.pk,
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkbook/AddTransaction.html')
        self.assertTrue(response.context['form'].errors['amount'])
        self.assertEqual(Transaction.TransactionDetails.count(), 0)

    def test_negative_opening_deposit_is_rejected(self):
        account_count = Accounts.Accounts.count()
        response = self.client.post(reverse('create'), {
            'first_name': 'New', 'last_name': 'Account', 'initial_deposit': '-0.01',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].errors['initial_deposit'])
        self.assertContains(response, 'Ensure this value is greater than or equal to 0.00.')
        self.assertEqual(Accounts.Accounts.count(), account_count)

    def test_zero_opening_deposit_is_allowed(self):
        response = self.client.post(reverse('create'), {
            'first_name': 'Zero', 'last_name': 'Account', 'initial_deposit': '0.00',
        })

        self.assertRedirects(response, reverse('index'))
        account = Accounts.Accounts.get(first_name='Zero')
        self.assertEqual(account.initial_deposit, Decimal('0.00'))

    def test_negative_and_zero_transactions_are_rejected(self):
        # Both types require a positive amount; the type supplies the direction.
        for transaction_type in ('Deposit', 'Withdraw'):
            for amount in ('-0.01', '0.00'):
                with self.subTest(transaction_type=transaction_type, amount=amount):
                    response = self.client.post(reverse('transaction'), {
                        'date': '2026-11-27', 'type': transaction_type,
                        'amount': amount, 'description': 'Invalid amount',
                        'account': self.account.pk,
                    })

                    self.assertEqual(response.status_code, 200)
                    self.assertTrue(response.context['form'].errors['amount'])
                    self.assertContains(response, 'Ensure this value is greater than or equal to 0.01.')

        self.assertEqual(Transaction.TransactionDetails.count(), 0)

    def test_smallest_positive_transaction_amount_is_allowed(self):
        for transaction_type in ('Deposit', 'Withdraw'):
            with self.subTest(transaction_type=transaction_type):
                response = self.client.post(reverse('transaction'), {
                    'date': '2026-11-27', 'type': transaction_type,
                    'amount': '0.01', 'description': 'Minimum amount',
                    'account': self.account.pk,
                })

                self.assertRedirects(response, reverse('balance', kwargs={'pk': self.account.pk}))

        self.assertEqual(Transaction.TransactionDetails.count(), 2)

    def test_empty_posts_show_required_errors_without_saving(self):
        account_count = Accounts.Accounts.count()
        required_fields = {
            'index': {'account'},
            'create': {'first_name', 'last_name', 'initial_deposit'},
            'transaction': {'date', 'type', 'amount', 'description', 'account'},
        }

        # No form data at all must still create a bound form with required errors.
        for name, fields in required_fields.items():
            with self.subTest(page=name):
                response = self.client.post(reverse(name), {})
                form = response.context['form']

                self.assertEqual(response.status_code, 200)
                self.assertTrue(form.is_bound)
                self.assertEqual(set(form.errors), fields)
                for field in fields:
                    self.assertEqual(form.errors.as_data()[field][0].code, 'required')
                self.assertContains(response, 'This field is required.', count=len(fields))

        self.assertEqual(Accounts.Accounts.count(), account_count)
        self.assertEqual(Transaction.TransactionDetails.count(), 0)

    def test_get_requests_show_forms_without_errors(self):
        # Simply opening a page must not display missing-field errors.
        for name in ('index', 'create', 'transaction'):
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                form = response.context['form']

                self.assertEqual(response.status_code, 200)
                self.assertFalse(form.is_bound)
                self.assertFalse(form.errors)
                self.assertNotContains(response, 'This field is required.')
