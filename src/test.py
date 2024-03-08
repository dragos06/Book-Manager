import unittest
from src.domain.domain import Book
from src.repository.mem_repo import MemoryRepository
from src.service.service import Service


class UnitTesting(unittest.TestCase):
    def setUp(self):
        self.repository = MemoryRepository()
        self.service = Service(self.repository)

    def test_add_book(self):
        self.service.add_book('1', 'Cowboy', 'John Wayne')
        self.assertEqual(self.service.get_all(), [Book('1', 'Cowboy', 'John Wayne')])

        self.service.add_book('2', 'Gestapo', 'Sven Hassel')
        self.assertEqual(self.service.get_all(),
                         [Book('1', 'Cowboy', 'John Wayne'), Book('2', 'Gestapo', 'Sven Hassel')])

        self.service.add_book('3', '1984', 'George Orwell')
        self.assertEqual(self.service.get_all(),
                         [Book('1', 'Cowboy', 'John Wayne'), Book('2', 'Gestapo', 'Sven Hassel'),
                          Book('3', '1984', 'George Orwell')])


if __name__ == '__main__':
    unittest.main()
