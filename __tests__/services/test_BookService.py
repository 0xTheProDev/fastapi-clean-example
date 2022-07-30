from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from services.BookService import BookService


class TestBookService(TestCase):
    authorRepository: AuthorRepository
    bookRepository: BookRepository
    bookService: BookService

    def setUp(self):
        super().setUp()
        self.authorRepository = create_autospec(
            AuthorRepository
        )
        self.bookRepository = create_autospec(
            BookRepository
        )
        self.bookService = BookService(
            self.authorRepository, self.bookRepository
        )

    @patch(
        "schemas.pydantic.BookSchema.BookSchema",
        autospec=True,
    )
    def test_create(self, BookSchema):
        book = BookSchema()
        book.name = "Harry Potter and The Order of Phoenix"

        self.bookService.create(book)

        # Should call create method on Book Repository
        self.bookRepository.create.assert_called_once()

    def test_delete(self):
        self.bookService.delete(book_id=1)

        # Should call delete method on Book Repository
        self.bookRepository.delete.assert_called_once()

    def test_get(self):
        self.bookService.get(book_id=1)

        # Should call get method on Book Repository
        self.bookRepository.get.assert_called_once()

    def test_list(self):
        name = "The Richest Man in Babylon"
        pageSize = 10
        startIndex = 2

        self.bookService.list(name, pageSize, startIndex)

        # Should call list method on Book Repository
        self.bookRepository.list.assert_called_once_with(
            name, pageSize, startIndex
        )

    @patch(
        "schemas.pydantic.BookSchema.BookSchema",
        autospec=True,
    )
    def test_update(self, BookSchema):
        book = BookSchema()
        book.name = "Harry Potter and The Order of Phoenix"

        self.bookService.update(book_id=1, book_body=book)

        # Should call update method on Book Repository
        self.bookRepository.update.assert_called_once()

    def test_get_authors(self):
        self.bookService.get_authors(book_id=1)

        # Should call get method on Book Repository
        self.bookRepository.get.assert_called_once()

    @patch(
        "schemas.pydantic.BookSchema.BookAuthorPostRequestSchema",
        autospec=True,
    )
    def test_add_author(self, BookAuthorPostRequestSchema):
        author = BookAuthorPostRequestSchema()
        author.author_id = 3

        self.bookService.add_author(
            book_id=1, author_body=author
        )

        # Should call get method on Author Repository
        self.authorRepository.get.assert_called_once()

        # Should call get method on Book Repository
        self.bookRepository.get.assert_called_once()

        # Should call update method on Book Repository
        self.bookRepository.update.assert_called_once()

    def test_remove_author(self):
        self.bookService.remove_author(
            book_id=1, author_id=2
        )

        # Should call get method on Book Repository
        self.bookRepository.get.assert_called_once()

        # Should call update method on Book Repository
        self.bookRepository.update.assert_called_once()
