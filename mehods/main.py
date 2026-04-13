
############################################################################################
#   File            :   oop.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   12/04/2026
#   Version         :   1.0.0
############################################################################################
#   Description:
#   This example shows the problem of keeping sharing value among same class type
#  
#-------------------------------------------------------------------------------------------
# License:
#     © 2026 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_book(self): 
        return self
    

### usage
b1 = Book("Python", "John", "1234567890")
b2 = Book("Java", "Mike", "1234567890123")

print(b1.get_book().title)
print(b2.get_book().title)


### how to calculate number of books ??


