from library.book import Book
from library.user import User
from library.librarian import Librarian

mimi = User(1001, "Mimi", 9)
print(mimi)
mimi.scan()

ba = Book(901, "A book")
bb = Book(902, "B book")
bc = Book(903, "C book")
bd = Book(904, "D book")

mimi.borrowBook(901)
mimi.borrowBook(902)
print(mimi.books)
mimi.returnBook(902)

admin = Librarian(0, "Admin")
print(admin)
admin.lendBooks(mimi, [902, 903, 904])
print(mimi.books)

# lend books to read
# print each users' reading books