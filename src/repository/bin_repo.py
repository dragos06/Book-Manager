import pickle
import os

from src.repository.mem_repo import MemoryRepository


class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.load_books_from_file()
        self._prev_book_list = []

    def load_books_from_file(self):
        try:
            if os.path.exists(self.__file_name):
                file = open(self.__file_name, 'rb')
                self._book_list = pickle.load(file)
                file.close()
        except EOFError:
            raise FileNotFoundError("File not found")

    def save_books_to_file(self):
        file = open(self.__file_name, 'wb')
        pickle.dump(self._book_list, file)
