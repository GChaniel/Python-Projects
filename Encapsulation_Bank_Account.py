
# Create a class for a bank account.
class BankAccount:

    # Initialise the account
    def __init__(self):
        self._accountHolder = "Isaac"
        self.__balance = 100

    def getBalance(self):
        print(self.__balance)

    # Add money to the account balance
    def deposit(self, amount):
        self.__balance = self.__balance + amount

# Create a bank account object
account = BankAccount()

# Display the account holders name
print(account._accountHolder)

#Deposit money and display the updated amount
account.deposit(50)
account.getBalance()
