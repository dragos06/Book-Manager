import os

from src.repository.mem_repo import MemoryRepository
from src.domain.domain import Book


class TextFileRepository(MemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_books_from_file()
        self._prev_book_list = []

    def load_books_from_file(self):
        try:
            if os.path.exists(self.__file_name):
                file = open(self.__file_name, 'r')
                lines = file.readlines()
                for line in lines:
                    isbn, title, author = line.strip().split(',')
                    self.add(Book(isbn, title, author))
        except EOFError:
            raise FileNotFoundError("File not found")

    def save_books_to_file(self):
        file = open(self.__file_name, 'w')
        for book in self._book_list:
            file.write(f"{book.get_isbn},{book.get_title},{book.get_author}\n")
