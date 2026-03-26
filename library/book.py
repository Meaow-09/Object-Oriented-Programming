class Book:
    def __init__(self, bID: int, name: str):
        self._bID = bID
        self._name = name
        self.is_available = True

    @property
    def bID(self):
        return self._bID

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"ID: {self.bID}\n   -Name: {self.name}"