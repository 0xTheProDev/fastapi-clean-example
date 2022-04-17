from typing import List, Optional

from fastapi import Depends

from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from schemas.AuthorSchema import AuthorSchema
from schemas.BookSchema import BookSchema


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

    def create(self, book: BookSchema) -> BookSchema:
        return self.bookRepository.create(book).id

    def delete(self, book_id: int) -> None:
        return self.bookRepository.delete(book_id)

    def get(self, book_id: int) -> BookSchema:
        return self.bookRepository.get(book_id).normalize()

    def list(
        self,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[BookSchema]:
        return [
            book.normalize()
            for book in self.bookRepository.list(
                pageSize, startIndex
            )
        ]

    def update(
        self, book_id: int, book: BookSchema
    ) -> BookSchema:
        return self.bookRepository.update(
            book_id, book
        ).normalize()

    def get_authors(
        self, book_id: int
    ) -> List[AuthorSchema]:
        return [
            author.normalize()
            for author in self.bookRepository.get(
                book_id
            ).authors
        ]

    def add_author(
        self, book_id: int, author_data: AuthorSchema
    ) -> List[AuthorSchema]:
        author = self.authorRepository.get(author_data.id)
        if author == None:
            author = self.authorRepository.create(
                author_data
            )

        book = self.bookRepository.get(book_id)
        book.authors.append(author)
        self.bookRepository.update(book_id, book)

        return [
            author.normalize() for author in book.authors
        ]

    def remove_author(self, book_id: int, author_id: int):
        book = self.bookRepository.get(book_id)
        book.authors = filter(
            lambda author: author.id != author_id,
            book.authors,
        )
        self.bookRepository.update(book_id, book)

        return [
            author.normalize() for author in book.authors
        ]
