class User:
    def __init__(self, id: int, name: str, group: int):
        self._id = id
        self._name = name
        self._group = group

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    def __str__(self):
        return "Member: " + self._name + ", ID: " + str(self._id) + ", Group: " + str(self._group)

    def scan(self):
        print("**", self._id, "is scanning. **")
        pass

    def borrowBook(self, bID: int):
        print(self._id, "is borrowing", bID)
        pass

    def returnBook(self, bID: int):
        print(self._id, " s returning", bID)
        pass


class Librarian(User):
    def __init__(self, empId: int, name: str, group: int):
        self.super(empId, name, group)

    @property
    def empId(self):
        return self._id



if __name__ == "__main__":
    user = User(1, "Mimi", 9)
    print(user)
    user.scan()
    user.borrowBook(10086)
