from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.BookRepository import BookRepository


class TestBookRepository(TestCase):
    session: Session
    bookRepository: BookRepository

    def setUp(self):
        super().setUp()
        self.session = create_autospec(Session)
        self.bookRepository = BookRepository(self.session)

    @patch("models.BookModel.Book", autospec=True)
    def test_create(self, Book):
        book = Book(
            name="Harry Potter and The Order of Phoenix"
        )
        self.bookRepository.create(book)

        # Should call add method on Session
        self.session.add.assert_called_once_with(book)

    @patch("models.BookModel.Book", autospec=True)
    def test_delete(self, Book):
        book = Book(id=1)
        self.bookRepository.delete(book)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(book)

    @patch("models.BookModel.Book", autospec=True)
    def test_get(self, Book):
        book = Book(id=1)
        self.bookRepository.get(book)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.BookModel.Book", autospec=True)
    def test_list(self, Book):
        self.bookRepository.list(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.bookRepository.list("Peaky Blinders", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(
            Book
        ).filter_by.assert_called_once_with(
            name="Peaky Blinders"
        )

    @patch("models.BookModel.Book", autospec=True)
    def test_update(self, Book):
        book = Book(name="The Wealth of Nations")
        self.bookRepository.update(id=1, book=book)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(book)
