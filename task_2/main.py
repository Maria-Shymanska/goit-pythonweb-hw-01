import logging
from abc import ABC, abstractmethod

# Налаштування логера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Принцип єдиної відповідальності (SRP)
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

# Принцип розділення інтерфейсів (ISP)
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass

# Принцип відкритості/закритості (OCP) та підстановки Лісков (LSP)
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        logger.info(f'Added book: {book}')

    def remove_book(self, title: str):
        before_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < before_count:
            logger.info(f'Removed book with title: {title}')
        else:
            logger.warning(f'Book with title {title} not found')

    def show_books(self):
        if not self.books:
            logger.info("No books available in the library.")
        for book in self.books:
            print(book)

# Принцип інверсії залежностей (DIP)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting program")
                break
            case _:
                logger.warning("Invalid command entered.")
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
