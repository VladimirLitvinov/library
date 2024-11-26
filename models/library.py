import json
import os
from typing import Dict, List

from .book import Book


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self, filename: str = 'library.json'):
        """
        Инициализация библиотеки.

        :param filename: Имя файла для хранения данных библиотеки.
        """
        self.filename = filename
        self.books: Dict[int, Book] = {}
        self.next_id = 1
        self.load_books()

    def load_books(self) -> None:
        """Загружает книги из файла JSON."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for book_data in data:
                    book = Book.from_dict(book_data)
                    self.books[book.id] = book
                    if book.id >= self.next_id:
                        self.next_id = book.id + 1

    def save_books(self) -> None:
        """Сохраняет книги в файл JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books.values()], file,
                      ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в библиотеку."""
        book = Book(self.next_id, title, author, year)
        self.books[self.next_id] = book
        self.next_id += 1
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {book.id}.")

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки по ID."""
        if book_id in self.books:
            del self.books[book_id]
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Ошибка: Книга с ID {book_id} не найдена.")

    def search_books(self, search_term: str) -> List | None:
        """Ищет книги по названию, автору или году."""
        results = [book for book in self.books.values() if
                   search_term in book.title or
                   search_term in book.author or search_term == str(
                       book.year)]
        if results:
            print("Результаты поиска:")
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")

        return results

    def display_books(self) -> None:
        """Отображает все книги в библиотеке."""
        if self.books:
            print("Список всех книг:")
            for book in self.books.values():
                print(book)
        else:
            print("Библиотека пуста.")

    def change_status(self, book_id: int, new_status: str) -> None:
        """Изменяет статус книги по ID."""
        if book_id in self.books and new_status in ["в наличии", "выдана"]:
            self.books[book_id].status = new_status
            self.save_books()
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
        else:
            print(
                f"Ошибка: Книга с ID {book_id} не найдена или статус '{new_status}' недопустим.")
