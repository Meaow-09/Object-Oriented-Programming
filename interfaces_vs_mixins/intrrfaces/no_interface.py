############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   07/04/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#     This module shows how we can use abstract base classes without defining a formal interface in Python.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

## In Python, we can achieve polymorphism without defining a formal interface.
class EmailNotification:
    def send(self, message):
        print("Sending Email:", message)
        ## implement the send method here


## Another class with the same method name but no formal interface
class SMSNotification:
    def send(self, message):
        print("Sending SMS:", message)
        ## implement the send method here

class AnroidNotification:
    def send_msg(self, message):
        print("Sending **:", message)
        ## implement the send method here

# Example usage
email = EmailNotification() ## Polymorphic behavior: EmailNotification has a send method
sms = SMSNotification() ## Polymorphic behavior: SMSNotification has a send method
ans=AnroidNotification()

ans.send_msg("this is my message")

email.send("Your book is due!")
sms.send("Your book is due!")