from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

# Create the Account models.
class Accounts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # An account can start at zero, but its opening deposit cannot be negative.
    # ModelForm uses this validator to display an error before saving.
    initial_deposit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
    )

    # Defines the model Manager for accounts
    Accounts = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Choices for a transaction
TransactionTypes = [('Deposit','Deposit'),('Withdraw','Withdraw')]


# Creates the transaction model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(choices=TransactionTypes, max_length=10)
    # The transaction type controls whether money is added or subtracted.
    # Keep the amount positive so a negative withdrawal cannot increase the balance.
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)

    #Defines the model Manager for transactions
    TransactionDetails = models.Manager()
