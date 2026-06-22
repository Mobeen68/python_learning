from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        for book in self.books:
            print(book)
    
    def remove_book(self, title):
        self.books = list(
            filter(lambda book: book.title != title, self.books)
        )
            
    
library = Library()

library.add_book(Book("Clean Code", "Robert Martin"))
library.add_book(Book("Python Basics", "Guido"))

library.show_books()

library.remove_book('Clean Code')

library.show_books()