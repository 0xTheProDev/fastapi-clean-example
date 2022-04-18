from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.AuthorModel import Author


class AuthorRepository:
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
    ) -> List[Author]:
        query = self.db.query(Author)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, author: Author) -> Author:
        return self.db.get(
            Author,
            author.id,
            options=[lazyload(Author.books)],
        )

    def create(self, author: Author) -> Author:
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        return author

    def update(self, id: int, author: Author) -> Author:
        author.id = id
        self.db.merge(author)
        self.db.commit()
        return author

    def delete(self, author: Author) -> None:
        self.db.delete(author)
        self.db.commit()
        self.db.flush()
