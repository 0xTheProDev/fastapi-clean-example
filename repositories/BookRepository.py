from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from dependencies.DatabaseConnection import get_db_connection
from models.BookModel import Book
from schemas.BookSchema import BookSchema

class BookRepository():
  db: Session
  
  def __init__(self, db: Session = Depends(get_db_connection)) -> None:
    self.db = db

  def get_all(self, limit: int, start: int) -> List[BookSchema]:
    return [book.__dict__ for book in self.db.query(Book).offset(start).limit(limit).all()]

  def get_by_id(self, id: int) -> BookSchema:
    return self.db.get(Book, id).__dict__

  def create(self, body: BookSchema) -> BookSchema:
    book = Book(name=body.name)
    self.db.add(book)
    self.db.commit()
    self.db.refresh(book)
    return book.__dict__

  def update(self, id: int, body: BookSchema) -> BookSchema:
    book = self.db.get(Book, id)
    book.name = body.name
    self.db.commit()
    self.db.refresh(book)
    return book.__dict__

  def delete(self, id: int) -> None:
    book = self.db.get(Book, id)
    self.db.delete(book)
    self.db.commit()
    self.db.flush()
