from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Accounts, Transaction

# This function will render the Home page when requested
def home(request):
    # Reuse the transaction form because its account field already lists saved accounts.
    # Check the request method so even an empty POST is validated; GET stays blank.
    form = TransactionForm(data=request.POST if request.method == 'POST' else None)

    # Keep only the account field on this form instance, so other transaction
    # fields are not required when the user simply chooses an account.
    form.fields = {'account': form.fields['account']}

    if request.method == 'POST':
        if form.is_valid():
            # The validated dropdown value is an Accounts object; pk is its ID.
            account = form.cleaned_data['account']
            # Redirect to the account URL so refreshing does not repeat the POST.
            return redirect('balance', pk=account.pk)

    # Choosing an account does not save the form or create a transaction.
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

# This function will render the Create New account page when requested
def create_account(request):
    # Bind every POST, including empty data, so missing fields produce errors.
    # Passing None on GET displays the form without validation errors.
    form = AccountForm(data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request, pk):
    # Find the account from the URL, or show a 404 page if it does not exist.
    account = get_object_or_404(Accounts, pk=pk)

    # Fetch only this account's transactions, oldest first. The ID breaks date ties.
    transactions = Transaction.TransactionDetails.filter(account=pk).order_by('date', 'pk')

    # Start with the opening deposit, then calculate a balance after each transaction.
    current_total = account.initial_deposit
    table_contents = {}
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
        else:
            current_total -= t.amount

        # Pair each transaction with the running balance after applying its amount.
        table_contents.update({t: current_total})

    # Pass the selected account, transaction rows, and final balance to the template.
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# This function will render the transaction page when requested
def transactions(request):
    # An empty POST is still a submission and must show required-field errors.
    # Only GET requests receive a blank, unbound form.
    form = TransactionForm(data=request.POST if request.method == 'POST' else None)
    if request.method == 'POST':
        if form.is_valid():
            # Save the valid form and keep the transaction object returned by Django.
            transaction = form.save()
            # account_id is the selected account's primary key (pk).
            # Redirect to its balance sheet so refreshing does not submit the form again.
            return redirect('balance', pk=transaction.account_id)
    # Pass content to the template in a dictionary
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
