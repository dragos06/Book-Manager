class Book:
    def __init__(self, isbn, title, author):
        self.__isbn = isbn
        self.__title = title
        self.__author = author

    def __str__(self):
        return f"{self.__isbn}: '{self.__title}' by {self.__author}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__isbn == other.get_isbn

    @property
    def get_isbn(self):
        return self.__isbn

    @property
    def get_author(self):
        return self.__author

    @property
    def get_title(self):
        return self.__title
