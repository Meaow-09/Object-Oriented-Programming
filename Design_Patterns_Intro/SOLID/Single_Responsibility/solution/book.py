class Book:
    def __init__(self, title, author, bID):
        self.title = title
        self.author = author
        self.bID = bID

    def __str__(self):
        return f"{self.title} by {self.author}, ID: {self.bID}"