from library.book import Book
from library.lending import Lending

class DuplicateBookException(Exception):
    def __init__(self):
        super().__init__("Book already exists")

class LibrarySystem:
    def __init__(self):
        self.books = {'bID': None, 'name': None}
        self.members = []
        self.lendings = []

    def add_book(self, book: Book):
        try:
            tempval = self.books[book.bID]
            raise DuplicateBookException
        except KeyError:
            self.books[book.bID] = book.name

    def add_member(self, member):
        self.members.append(member)

    def lend_book(self, book_id, member_id):
        book = next((b for b in self.books if b.ID == book_id), None)
        member = next((m for m in self.members if m.ID == member_id), None)

        if book and member and book.is_available:
            lending = Lending(book, member)
            self.lendings.append(lending)
            book.is_available = False
            print("Book lent successfully")
        else:
            print("Opps...Cannot lend book")

    def show_data(self):
        print("\n--- Books ---")
        for b in self.books:
            print(b)

        print("\n--- Members ---")
        print(f"There are {len(self.members)} registered")
        for m in self.members:
            print(m)

        print("\n--- Lendings ---")
        for l in self.lendings:
            print(l)
