from copy import deepcopy
from src.domain.domain import Book


class MemoryRepository:
    def __init__(self):
        self._book_list = []
        self._prev_book_list = []

    def search_by_isbn(self, isbn):
        for book in self._book_list:
            if book.get_isbn == isbn:
                return book
        return None

    def search_by_starts_with_title(self, title):
        for book in self._book_list:
            if book.get_title.lower().startswith(title.strip().lower()):
                return book
        return None

    def add(self, book: Book) -> None:
        """
        Adds the book to the current repository
        :param book: A book object containing the isbn, title and author of the book
        :return: None
        """
        if self.search_by_isbn(book.get_isbn):
            raise ValueError("This book already exists")
        self._prev_book_list.append(deepcopy(self._book_list))
        self._book_list.append(book)

    def filter_by_title(self, title):
        if not self.search_by_starts_with_title(title):
            raise ValueError("Books not found to filter by")
        self._prev_book_list.append(deepcopy(self._book_list))
        self._book_list = [book for book in self._book_list if
                           not (book.get_title.lower()).startswith(title.lower().strip())]

    def undo(self):
        if self._prev_book_list:
            self._book_list = self._prev_book_list.pop()
        else:
            raise ValueError("Undo not possible")

    def get_all(self):
        return self._book_list.copy()

    def length_of_book_list(self):
        return len(self._book_list)
