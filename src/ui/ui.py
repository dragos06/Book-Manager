from src.domain.domain import Book


class Ui:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def print_menu():
        print("1. Add a book. Book data is read from the console.")
        print("2. Display the list of books")
        print(
            "3. Filter the list so that book titles starting with a given word are deleted from the list.")
        print(
            "4. Undo the last operation that modified program data. This step can be repeated. The user can undo only"
            "those operations made during the current run of the program.")
        print("5. Exit")

    def add_book(self):
        new_isbn = input("Please enter the isbn: ")
        new_title = input("Please enter the title: ")
        new_author = input("Please enter the author: ")
        self.__service.add_book(new_isbn, new_title, new_author)

    def list_books(self):
        for book in self.__service.get_all():
            print(book)

    def filter(self):
        title_to_filter_by = input("Please enter the word by which the list will be filtered: ")
        self.__service.filter_by_title(title_to_filter_by)

    def undo(self):
        self.__service.undo()

    def start(self):
        self.print_menu()
        if self.__service.is_empty():
            self.__service.generate_startup_list()
        while True:
            try:
                user_option = input("Please select an option: ")
                if user_option == '1':
                    self.add_book()
                elif user_option == '2':
                    self.list_books()
                elif user_option == '3':
                    self.filter()
                elif user_option == '4':
                    self.undo()
                elif user_option == '5':
                    print("Exiting...")
                    break
                else:
                    print("Invalid input!")
            except ValueError as e:
                print("Error occurred: ", e)
