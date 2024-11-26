from typing import Dict


class Book:
    """Класс для представления книги в библиотеке."""

    def __init__(self, book_id: int, title: str, author: str, year: int):
        """
        Инициализация книги.

        :param book_id: Уникальный идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def to_dict(self) -> Dict:
        """Преобразует книгу в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """Создает объект книги из словаря."""
        book = Book(data["id"], data["title"], data["author"], data["year"])
        book.status = data["status"]
        return book

    def __repr__(self) -> str:
        """Возвращает строковое представление книги."""
        return (
            f"ID: {self.id}, Title: '{self.title}', Author: '{self.author}', "
            f"Year: {self.year}, Status: '{self.status}'")
