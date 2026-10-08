class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Warning: Balance cannot be negative.")

account = BankAccount("123456789", 5000)

print("Account Number:", account.account_number)
print("Balance:", f"₱{account.balance:,.2f}")

account.account_number = "987654321"
account.balance = 7500

print("Account Number:", account.account_number)
print("Balance:", f"₱{account.balance:,.2f}")

account.balance = -1000
