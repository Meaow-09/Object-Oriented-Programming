from bankaccount import BankAccount

class JounionAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def account_type(self):
        return "Jounion Account"

    def deposit(self, amount):
        print("We are welcome for you to deposit in Jounion Account! We will give you 1 extra unit for your deposit!")
        return super().deposit(amount + 1)

    def withdraw(self, amount):
        print("We are sorry to see you withdraw from Jounion Account! We will charge you 2 extra unit for your withdrawal!")
        return super().withdraw(amount + 2)