from library.user import User


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
