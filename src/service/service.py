from src.domain.domain import Book
from src.repository.txt_repo import TextFileRepository
from src.repository.bin_repo import BinaryFileRepository


class Service:
    def __init__(self, repository):
        self.__repository = repository

    def add_book(self, isbn: str, title: str, author: str) -> None:
        """
        Adds a book to the repository and saves it to file in case of file-backed repository
        :param isbn: The isbn of the book
        :param title: The title of the book
        :param author: The author of the book
        :return: A Book containing isbn, title and author
        """
        book = Book(isbn, title, author)
        self.__repository.add(book)
        self.save_books_to_file()

    def filter_by_title(self, title):
        self.__repository.filter_by_title(title)
        self.save_books_to_file()

    def get_all(self):
        return self.__repository.get_all()

    def undo(self):
        self.__repository.undo()
        self.save_books_to_file()

    def save_books_to_file(self):
        if isinstance(self.__repository, TextFileRepository) or isinstance(self.__repository, BinaryFileRepository):
            self.__repository.save_books_to_file()

    def is_empty(self):
        if self.__repository.length_of_book_list() == 0:
            return True
        return False

    def generate_startup_list(self):
        self.add_book("1", "Big Cowboys", "John Wayne")
        self.add_book("2", "Gestapo", "Sven Hassel")
        self.add_book("3", "Jane Eyre", "Charlotte Bronte")
        self.add_book("4", "1984", "George Orwell")
        self.add_book("5", "To Kill a Mockingbird", "Harper Lee")
        self.add_book("6", "The Great Gatsby", "F. Scott Fitzgerald")
        self.add_book("7", "The Harry Potter Series", "J.K Rowling")
        self.add_book("8", "The Lord of the Rings", "J.R.R. Tolkien")
        self.add_book("9", "The Alchemist", "Paulo Coelho")
        self.add_book("10", "Pride and Prejudice", "Jane Austen")
        self.__repository._prev_book_list = []
