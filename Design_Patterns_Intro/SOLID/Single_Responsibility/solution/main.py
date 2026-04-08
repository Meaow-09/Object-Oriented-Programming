from Design_Patterns_Intro.SOLID.Single_Responsibility.solution.book import Book
from Design_Patterns_Intro.SOLID.Single_Responsibility.solution.book_printer import BookPrinter
from Design_Patterns_Intro.SOLID.Single_Responsibility.solution.book_repo import BookRepository

bookA = Book("BookA","AAA",1)
bookB = Book("BookB","BBB",2)

p = BookPrinter()
p.print(bookA)

rep = BookRepository()
rep.save(bookA)
print(rep.retrieve(3))