import pickle

from library.book import Book
from library.user import User
from library.librarian import Librarian


def tryBorrowBook(user: User, book):
    try:
        return user.borrowBook(book)
    except Exception as err:
        print(err)


def tryReturnBook(user: User, book):
    try:
        return user.returnBook(book)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    mimi = User(1001, "Mimi", 9)
    print(mimi)
    mimi.scan()

    ### try to load the user from the serialized obj
    with open("./mimi.pkl", mode="rb") as file:
        user1 = pickle.load(file)

    ### serialize the user
    with open("./mimi.pkl", mode="wb") as file:
        pickle.dump(user1, file)
    user1.scan()

    ba = Book(901, "A book")
    bb = Book(902, "B book")
    bc = Book(903, "C book")
    bd = Book(904, "D book")

    tryBorrowBook(mimi, ba)
    tryBorrowBook(mimi, bb)
    tryBorrowBook(mimi, bb)

    tryReturnBook(mimi, bc)
    tryBorrowBook(mimi, bc)
    tryBorrowBook(mimi, bd)

    mimi.showBooks()

    try:
        me = User(10011, "me", 1)
    except Exception as err:
        print(err)

    # admin = Librarian(0, "Admin")
    # print(admin)
    # admin.lendBooks(mimi, [902, 903, 904])
    # print(mimi.books)

    # lend books to read
    # print each users' reading books
