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

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private
        self.__cur_balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")

    @property
    def cur_balance(self):
        return self.__cur_balance

    @cur_balance.setter
    def cur_balance(self, value):
        self.__cur_balance = value

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.update()
            print(f"{self.name} deposited {amount}. New balance: {self.__cur_balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.update()
            print(f"{self.name} withdrew {amount}. New balance: {self.__cur_balance}")
            return True
        else:
            print("Insufficient balance or invalid amount!")
            return False

    def update(self):
        self.cur_balance = self.balance

    def transfer(self, amount, other):
        print(self.name + "is transferring " + str(amount) + " to " + other._name)
        if self.withdraw(amount):
            print("*** Transferring ***")
            other.deposit(amount)
            return True
        else:
            print("Insufficient balance or invalid amount!")
            return False


    # Abstract method to show account type
    @abstractmethod
    def account_type(self):
        pass

