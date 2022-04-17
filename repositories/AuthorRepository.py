from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from dependencies.DatabaseConnection import (
    get_db_connection,
)
from models.AuthorModel import Author
from schemas.AuthorSchema import AuthorSchema


class AuthorRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(self, limit: int, start: int) -> List[Author]:
        self.db.query(Author).offset(start).limit(
            limit
        ).all()

    def get(self, id: int) -> Author:
        return self.db.get(Author, id)

    def create(self, body: AuthorSchema) -> Author:
        author = Author(name=body.name)
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        return author

    def update(self, id: int, body: AuthorSchema) -> Author:
        author = self.db.get(Author, id)
        author.name = body.name
        self.db.commit()
        self.db.refresh(author)
        return author

    def delete(self, id: int) -> None:
        author = self.db.get(Author, id)
        self.db.delete(author)
        self.db.commit()
        self.db.flush()
