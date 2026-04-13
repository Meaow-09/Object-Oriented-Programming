
class Book:
    total_books = 0   # class variable

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_books = 1

    ### Class Method
    @property
    def Total(self):
        return self.total_books ## return instance variable
    
    ### Class Method
    @classmethod
    def get_total_books(cls):
        return cls.total_books  ## return class variable

    ### Class Method
    @classmethod
    def add_book(cls):
        cls.total_books+=1

### usage
b1 = Book("Python", "John", "1234567890")
b2 = Book("Java", "Mike", "1234567890123")

print(b1.Total) ## read getter
print(b2.Total) ## read getter

print(b1.get_total_books()) ## call class level variable
print(b2.get_total_books()) ## call class level variable

b2.add_book() ### increment the class varaible
print(b2.get_total_books())



