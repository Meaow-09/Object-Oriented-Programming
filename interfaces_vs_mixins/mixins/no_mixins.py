
############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   07/04/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#     This module shows how we can implement complex behavior in Python without using mixins.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
 look for code complexity and duplication.
 Understand the maintainability of the code cost 
"""

## definne a class for email notifications
class EmailNotification:
    def log(self, message):
        print("[LOG]:", message)

    def format_message(self, message):
        return f"*** {message} ***"

    def send(self, message):
        formatted = self.format_message(message)
        self.log("Sending Email")
        print("Email:", formatted)


## define a class for SMS notifications
class SMSNotification:
    def log(self, message):
        print("[LOG]:", message)

    def send(self, message):
        self.log("Sending SMS")
        print("SMS:", message)


## Example usage
email = EmailNotification() ## creating an instance of EmailNotification
sms = SMSNotification() ## creating an instance of SMSNotification

email.send("Your book is due!")
print("-----")
sms.send("Your book is due!")