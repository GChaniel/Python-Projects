from django.forms import ModelForm
from .models import Accounts, Transaction

#Creates Account form based on account model
class AccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'


# Creates transaction form based on transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'