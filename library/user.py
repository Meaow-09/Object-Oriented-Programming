from library.book import Book


class User:
    def __init__(self, uID: int, name: str, group: int):
        self._uID = uID
        self._name = name
        self._group = group
        self._books = []

    @property
    def uID(self):
        return self._uID

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @property
    def books(self):
        return self._books

    def __str__(self):
        return "\t Member: " + self.name + ", ID: " + str(self.uID) + ", Group: " + str(self.group)

    def scan(self):
        print("**", self.uID, "is scanning. **")

    def borrowBook(self, book: Book):
        print("\t", self.name, "is borrowing", book.name)
        if book in self._books:
            # raise Exception('!!', self.uID, 'Already borrowed', book.bID, '!!')
            raise Exception(f"!! {self.uID} Already borrowed {book.bID} !!")

        if len(self.books) >= 3:
            # raise Exception('!!', self.uID, 'Failed to borrow', book.bID, ', can only borrow 3 books at a time. !!')
            raise Exception(f"!! {self.uID} Failed to borrow {book.bID}, can only borrow 3 books at a time. !!")

        self.books.append(book)
        print("**", self.uID, "Successfully borrowed", book.bID, "**")
        return True

    def returnBook(self, book: Book):
        print("\t", self.name, "is returning", book.name)
        if book in self._books:
            self.books.remove(book)
            print("**", self.uID, "Successfully returned", book.bID, "**")
            return True
        else:
            # raise Exception('!!', self.uID, 'Failed to return', book.bID, ', please check borrow list. !!')
            raise Exception(f"!! {self.uID} Failed to return {book.bID}, please check borrow list. !!")

    def showBooks(self):
        print("\t", self.uID, self.name, "borrowed:", end="\n|\t")
        for book in self.books:
            print(book.bID, "->", book.name, end="\t|\t")
