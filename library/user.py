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
        print(self.uID, "is returning", bID)
        if bID in self._books:
            self.books.remove(bID)
            print("** Successfully returned", bID, "**")
        else:
            print("!! Failed to return", bID, ", please check your borrow list. !!")
