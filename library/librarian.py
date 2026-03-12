from library.user import User


class Librarian(User):
    def __init__(self, empID: int, name: str):
        super().__init__(empID, name, 0)

    @property
    def empID(self):
        return self._uID

    def __str__(self):
        return "# Librarian: " + self._name + ", ID: " + str(self.empID) + ", Group: " + str(self.group)

    def manageUser(self, uID, action):
        print("#", self.empID, "is", action, uID)

    def manageBook(self, bID, action):
        print("#", self.empID, "is", action, bID)

    def changeOverdueBook(self, bID, uID):
        pass

    def lendBooks(self, user: User, books: list):
        user.books.extend(books)
        print("# Successfully borrowed", books)
