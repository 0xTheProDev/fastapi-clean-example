from fastapi import Depends
from typing import List, Optional

from repositories.BookRepository import BookRepository
from schemas.BookSchema import BookSchema

class BookService:
  bookRepository: BookRepository

  def __init__(self, bookRepository: BookRepository = Depends()) -> None:
    self.bookRepository = bookRepository

  def create(self, book: BookSchema) -> BookSchema:
    return self.bookRepository.create(book)

  def delete(self, book_id: int) -> None:
    return self.bookRepository.delete(book_id)

  def get(self, book_id: int) -> BookSchema:
    return self.bookRepository.get_by_id(book_id)

  def index(self, pageSize: Optional[int] = 100, startIndex: Optional[int] = 0) -> List[BookSchema]:
    return self.bookRepository.get_all(pageSize, startIndex)

  def update(self, book_id: int, book: BookSchema) -> BookSchema:
    return self.bookRepository.update(book_id, book)
