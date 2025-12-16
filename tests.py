import main
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_long_name_should_not_add(self):
        collector = BooksCollector()
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_book_should_not_add(self):
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_set_book_genre_with_invalid_genre_should_not_set(self):
        collector = BooksCollector()
        book_name = 'Книга без жанра'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Несуществующий жанр')
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')

        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Фантастика')
        collector.set_book_genre('Книга 3', 'Ужасы')

        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 2
        assert 'Книга 1' in fantasy_books
        assert 'Книга 2' in fantasy_books

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Детская книга 1')
        collector.add_new_book('Детская книга 2')
        collector.add_new_book('Взрослая книга')

        collector.set_book_genre('Детская книга 1', 'Мультфильмы')
        collector.set_book_genre('Детская книга 2', 'Комедии')
        collector.set_book_genre('Взрослая книга', 'Ужасы')

        children_books = collector.get_books_for_children()
        assert len(children_books) == 2
        assert 'Детская книга 1' in children_books
        assert 'Детская книга 2' in children_books
        assert 'Взрослая книга' not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Любимая книга'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert book_name in favorites

    def test_add_book_in_favorites_nonexistent_book_should_not_add(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Книга для удаления'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removal(self):
        collector = BooksCollector()
        book_name = 'Книга для удаления'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0

    @main.mark.parametrize('book_name,expected_count', [
        ('A' * 1, 1),
        ('A' * 40, 1),
        ('A' * 41, 0),
        ('', 0),
    ])
    def test_add_new_book_boundary_name_length(self, book_name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_count

    @main.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_valid_genres(self, genre):
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_empty_book_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_get_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_nonexistent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        result = collector.get_books_with_specific_genre('Несуществующий жанр')
        assert result == []

































