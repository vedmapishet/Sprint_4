from main import BooksCollector
import pytest
class TestBooksCollector:

    # Проверка метода add_new_book. Добавление 2 книг
    def test_add_new_book_add_two_books_true(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        assert len(collector.get_books_genre()) == 2

    # Проверка метода add_new_book. Одну и ту же книгу можно добавить один раз
    def test_add_new_book_add_one_book_true(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 1')
        assert len(collector.get_books_genre()) != 2

    #Параметризация. Название книги может содержать максимум 40 символов
    @pytest.mark.parametrize("name", ['', 'В книге должно быть не более сорока симво'])
    def test_add_new_book_not_valid_name_false(self, name, collector):
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    #Проверка метода set_book_genre
    def test_set_book_genre_add_genre_true(self, collector):
        collector.add_new_book('Книга ужасов')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        assert {'Книга ужасов': 'Ужасы'} == collector.get_books_genre()


    #Проверка метода get_book_genre
    def test_get_book_genre_get_genre_true(self, collector):
        collector.add_new_book('Книга ужасов')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        assert collector.get_book_genre('Книга ужасов') == 'Ужасы'

    #Проверка метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_get_list_true(self, collector):
        collector.add_new_book('Книга ужасов')
        collector.add_new_book('Оно')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Книга ужасов', 'Оно']


    #Проверка метода get_books_for_children.  Отображает книги для детей
    def test_get_books_for_children_get_list_true(self, collector):
        collector.add_new_book('Сказка на ночь')
        collector.add_new_book('Алиса что то там')
        collector.add_new_book('Один дома')
        collector.add_new_book('Книга ужасов')
        collector.set_book_genre('Сказка на ночь', 'Мультфильмы')
        collector.set_book_genre('Алиса что то там', 'Фантастика')
        collector.set_book_genre('Один дома', 'Комедии')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        assert len(collector.get_books_for_children()) == 3

    #Проверяем метод добавления книг в избранное
    def test_add_book_in_favorites_empty_list_list_increased(self, collector):
        collector.add_new_book('Пуаро')
        collector.set_book_genre('Пуаро', 'Детективы')
        collector.add_book_in_favorites('Пуаро')
        assert collector.get_list_of_favorites_books() == ['Пуаро']

    # Проверяем метод delete_book_from_favorites
    def test_delete_book_from_favorites_delete_book_true(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.delete_book_from_favorites('Книга 1')
        assert len(collector.favorites) == 0

    # Проверяем метод get_list_of_favorites_books
    def test_get_list_of_favorites_books_remove_books_true(self, collector):
        collector.add_new_book('Книга ужасов')
        collector.add_new_book('Пуаро')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        collector.set_book_genre('Пуаро', 'Детективы')
        collector.add_book_in_favorites('Книга ужасов')
        collector.add_book_in_favorites('Пуаро')
        assert len(collector.get_list_of_favorites_books()) == 2