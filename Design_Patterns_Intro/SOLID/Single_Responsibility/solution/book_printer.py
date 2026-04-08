from Design_Patterns_Intro.SOLID.Single_Responsibility.solution.book import Book


class BookPrinter:
    def print(self, book:Book):
        print(f"{self} printing: {book.title} by {book.author}, ID: {self.bID}")