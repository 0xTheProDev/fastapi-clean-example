from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.BookModel import Book


class BookRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Book]:
        query = self.db.query(Book)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, book: Book) -> Book:
        return self.db.get(
            Book, book.id, options=[lazyload(Book.authors)]
        )

    def create(self, book: Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, id: int, book: Book) -> Book:
        book.id = id
        self.db.merge(book)
        self.db.commit()
        return book

    def delete(self, book: Book) -> None:
        self.db.delete(book)
        self.db.commit()
        self.db.flush()
