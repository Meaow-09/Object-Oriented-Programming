class Book:
    def __init__(self, bID: int, name: str):
        self._bID = bID
        self._name = name

    @property
    def bID(self):
        return self._bID

    @property
    def name(self):
        return self._name


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
        return "Member: " + self.name + ", ID: " + str(self.uID) + ", Group: " + str(self.group)

    def scan(self):
        print("**", self.uID, "is scanning. **")

    def borrowBook(self, bID: int):
        print(self.uID, "is borrowing", bID)
        if len(self.books) <= 3:
            self.books.append(bID)
            print("** Successfully borrowed", bID, "**")
        else:
            print("!! Failed to borrow", bID, ", you can only borrow 3 books at a time. !!")

    def returnBook(self, bID: int):
        print(self.uID, " s returning", bID)
        if bID in self._books:
            self.books.remove(bID)
            print("** Successfully returned", bID, "**")
        else:
            print("!! Failed to return", bID, ", please check your borrow list. !!")


class Librarian(User):
    def __init__(self, empID: int, name: str):
        super().__init__(empID, name, 0)

    @property
    def empID(self):
        return self._uID

    def __str__(self):
        return "# Librarian: " + self._name + ", ID: " + str(self.empID) + ", Group: " + str(self.group)

    def manageUser(self, uID, action):
        print("**", self.empID, "is", action, uID, "**")

    def manageBook(self, bID, action):
        print("**", self.empID, "is", action, bID, "**")

    def changeOverdueBook(self, bID, uID):
        pass


class Read:
    def __init__(self, user: User, books: list):
        self._user = user
        self._books = books

    @property
    def uID(self):
        return self._user.uID

    @property
    def books(self):
        return self._books

    @property
    def booksCount(self):
        return len(self._books)


if __name__ == "__main__":
    mimi = User(1001, "Mimi", 9)
    print(mimi)
    mimi.scan()
    mimi.borrowBook(10086)
    print(mimi.books)
    mimi.returnBook(10086)

    admin = Librarian(0, "Admin")
    print(admin)

