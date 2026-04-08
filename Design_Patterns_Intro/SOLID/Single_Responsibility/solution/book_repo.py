### responsible for
###  saving and retrieving book data from a database
###  upload and download book data from network

### *** retrieve & store
from Design_Patterns_Intro.SOLID.Single_Responsibility.solution.book import Book


class BookRepository:
    def save(self, book):
        print("Saving book to database/file...")

    def retrieve(self, title, author, bID) -> Book:
        return Book(title, author, bID)

    def upload(self, book:Book):
        print(f"Uploading {book} to network...")

    def download(self, book:Book):
        print(f"Downloading {book} to network...")
        return book
