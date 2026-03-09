############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com,ajith.de-silva@epita.fr)
#   Created         :   23/02/2026
#   Last Modified   :   23/02/2206
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows usage of Inheritance to create a base class and extend it with derived classes.
#       We also show how to use abstract methods to enforce implementation in derived classes.
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from bankaccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit  #### negative balance allowed

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            #### allow overdraft
            self.balance -= amount
            self.update()
            print(f"{self.name} withdrew {amount}. New balance: {self.balance}")
            return True
        else:
            print("Withdrawal exceeds overdraft limit!")
            return False

    def account_type(self):
        return "Current Account"

    def transfer(self, amount, other):
        if 0 < amount <= self.balance:
            super().transfer(self, amount, other)
            return True
        elif self.balance < amount <= (self.balance + self.overdraft_limit):
            ta = amount
            amount -= self.balance
            self.balance = 0
            self.update()
            self.overdraft_limit -= amount
            print(f"{self.name} is transferring {ta} to {other._name}.\nNew balance: {self.balance}. New overdraft limit: {self.overdraft_limit}")
            print("*** Transferring ***")
            other.deposit(ta)
            return True
        else:
            print("Insufficient balance or invalid amount!")
            return False