from fastapi import Depends
from typing import List, Optional

from repositories.BookRepository import BookRepository
from schemas.AuthorSchema import AuthorSchema
from schemas.BookSchema import BookSchema

class BookService:
  bookRepository: BookRepository

  def __init__(self, bookRepository: BookRepository = Depends()) -> None:
    self.bookRepository = bookRepository

  def create(self, book: BookSchema) -> BookSchema:
    return self.bookRepository.create(book).id

  def delete(self, book_id: int) -> None:
    return self.bookRepository.delete(book_id)

  def get(self, book_id: int) -> BookSchema:
    return self.bookRepository.get(book_id).normalize()

  def list(self, pageSize: Optional[int] = 100, startIndex: Optional[int] = 0) -> List[BookSchema]:
    return [book.normalize() for book in self.bookRepository.list(pageSize, startIndex)]

  def update(self, book_id: int, book: BookSchema) -> BookSchema:
    return self.bookRepository.update(book_id, book).normalize()

  def get_author(self, book_id: int) -> List[AuthorSchema]:
    return [author.normalize() for author in self.bookRepository.get(book_id).authors]
