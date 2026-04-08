############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   07/04/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#     This module shows how we can use abstract base classes to define interfaces in Python.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from abc import ABC, abstractmethod
from email.mime import message

## Abstract Base Class (Interface)
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):    ### MUST implement by sub classes
        pass

    @abstractmethod
    def info(self):
        pass

## Concrete implementations of the interface
class EmailNotification(NotificationService):
    def send(self, message):
        print("Sending Email:", message)
        ## implement the send method here
    def info(self):
        print("I am Email info method")

## Concrete implementation of the interface
class SMSNotification(NotificationService):
    def send(self, message):
        print("Sending SMS:", message)
        ## implement the send method here

    def info(self):
        print("I am SMS info")

# Example usage
email = EmailNotification() ## Polymorphic behavior: EmailNotification is a NotificationService
email.send("Your book is due!")

sms = SMSNotification() ## Polymorphic behavior: SMSNotification is a NotificationService
sms.send("Your book is due!")   