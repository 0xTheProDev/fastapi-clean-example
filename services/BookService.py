from typing import List, Optional

from fastapi import Depends
from models.AuthorModel import Author
from models.BookModel import Book

from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from schemas.pydantic.AuthorSchema import AuthorSchema
from schemas.pydantic.BookSchema import (
    BookAuthorPostRequestSchema,
    BookSchema,
)


class BookService:
    authorRepository: AuthorRepository
    bookRepository: BookRepository

    def __init__(
        self,
        authorRepository: AuthorRepository = Depends(),
        bookRepository: BookRepository = Depends(),
    ) -> None:
        self.authorRepository = authorRepository
        self.bookRepository = bookRepository

    def create(self, book_body: BookSchema) -> Book:
        return self.bookRepository.create(
            Book(name=book_body.name)
        )

    def delete(self, book_id: int) -> None:
        return self.bookRepository.delete(Book(id=book_id))

    def get(self, book_id: int) -> Book:
        return self.bookRepository.get(Book(id=book_id))

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Book]:
        return self.bookRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, book_id: int, book_body: BookSchema
    ) -> Book:
        return self.bookRepository.update(
            book_id, Book(name=book_body.name)
        )

    def get_authors(self, book_id: int) -> List[Author]:
        return self.bookRepository.get(
            Book(id=book_id)
        ).authors

    def add_author(
        self,
        book_id: int,
        author_body: BookAuthorPostRequestSchema,
    ) -> List[Author]:
        author = self.authorRepository.get(
            Author(id=author_body.author_id)
        )
        book = self.bookRepository.get(Book(id=book_id))
        book.authors.append(author)
        self.bookRepository.update(book_id, book)

        return book.authors

    def remove_author(
        self, book_id: int, author_id: int
    ) -> List[Author]:
        book = self.bookRepository.get(Book(id=book_id))
        book.authors = filter(
            lambda author: author.id != author_id,
            book.authors,
        )
        self.bookRepository.update(book_id, book)

        return book.authors
