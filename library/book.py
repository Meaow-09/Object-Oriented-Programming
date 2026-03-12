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
