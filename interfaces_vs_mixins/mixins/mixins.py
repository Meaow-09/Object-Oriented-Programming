
############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   07/04/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#     This module shows how we can use mixins to add common functionality to multiple classes in Python.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

"""
    LoggerMixin → adds logging capability
    FormatMixin → adds message formatting
    Classes reuse behavior without rewriting code
"""
## We create classes that inherit from multiple mixins to combine their functionality.  
class LoggerMixin:
    def log(self, message):
        print("[LOG]:", message)


## We can create classes that inherit from multiple mixins to combine their functionality.
class FormatMixin:
    def format_message(self, message):
        return f"*** {message} ***"

## Now we can create notification classes that use both mixins.  
class EmailNotification(LoggerMixin, FormatMixin):
    def send(self, message):
        formatted = self.format_message(message)
        self.log("Sending Email")
        ## implement the send method here
        print("Email:", formatted)

## Another class that uses the same mixins to have logging and formatting capabilities.
class SMSNotification(LoggerMixin):
    def send(self, message):
        ## implement the send method here
        self.log("Sending SMS")
        print("SMS:", message)



## Example usage
email = EmailNotification() ## Polymorphic behavior: EmailNotification has log and format_message methods from mixins
sms = SMSNotification() ## Polymorphic behavior: SMSNotification has log method from LoggerMixin

email.send("Your book is due!")
print("-----")
sms.send("Your book is due!")