from models import Library


def main() -> None:
    """Основная функция для взаимодействия с пользователем через командную строку."""
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)
        elif choice == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
            except ValueError:
                print("Ошибка: Введите корректный ID.")
        elif choice == '3':
            search_term = input(
                "Введите название, автора или год для поиска: ")
            library.search_books(search_term)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id = int(
                    input("Введите ID книги для изменения статуса: "))
                new_status = input(
                    "Введите новый статус ('в наличии' или 'выдана'): ")
                library.change_status(book_id, new_status)
            except ValueError:
                print("Ошибка: Введите корректный ID.")
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
