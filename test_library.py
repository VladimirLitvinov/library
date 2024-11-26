import unittest
import os
from models.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library('test_library.json')
        self.library.add_book("Тестовая книга", "Тестовый автор", 2023)

    def tearDown(self):
        os.remove('test_library.json')

    def test_add_book(self):
        initial_count = len(self.library.books)
        self.library.add_book("Новая книга", "Новый автор", 2023)
        self.assertEqual(len(self.library.books), initial_count + 1)

    def test_remove_book(self):
        book_id = 1
        self.library.remove_book(book_id)
        self.assertNotIn(book_id, self.library.books)

    def test_search_books(self):
        results = self.library.search_books("Тестовая книга")
        self.assertGreater(len(results), 0)


if __name__ == '__main__':
    unittest.main()
