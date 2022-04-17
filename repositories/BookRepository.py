from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from dependencies.DatabaseConnection import (
    get_db_connection,
)
from models.BookModel import Book
from schemas.BookSchema import BookSchema


class BookRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(self, limit: int, start: int) -> List[Book]:
        return (
            self.db.query(Book)
            .offset(start)
            .limit(limit)
            .all()
        )

    def get(self, id: int) -> Book:
        return self.db.get(
            Book, id, options=[lazyload(Book.authors)]
        )

    def create(self, body: BookSchema) -> Book:
        book = Book(name=body.name)
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, id: int, body: BookSchema) -> Book:
        book = self.db.get(Book, id)
        book.name = body.name
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete(self, id: int) -> None:
        book = self.db.get(Book, id)
        self.db.delete(book)
        self.db.commit()
        self.db.flush()
