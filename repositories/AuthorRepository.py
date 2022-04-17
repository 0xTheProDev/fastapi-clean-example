from sqlalchemy.orm import Session
from typing import List

from models.AuthorModel import Author
from schemas.AuthorSchema import AuthorPostRequestSchema, AuthorPostResponseSchema, AuthorSchema

class AuthorRepository():
  @classmethod
  def get_all(self, db: Session, limit: int, start: int) -> List[AuthorSchema]:
    return [author.__dict__ for author in db.query(Author).offset(start).limit(limit).all()]

  @classmethod
  def get_by_id(self, db: Session, id: int) -> AuthorSchema:
    return db.get(Author, id).__dict__

  @classmethod
  def create(self, db: Session, body: AuthorPostRequestSchema) -> AuthorPostResponseSchema:
    author = Author(name=body.name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author.__dict__

  @classmethod
  def update(self, db: Session, id: int, body: AuthorPostRequestSchema) -> AuthorSchema:
    author = db.get(Author, id)
    author.name = body.name
    db.commit()
    db.refresh(author)
    return author.__dict__

  @classmethod
  def delete(self, db: Session, id: int) -> None:
    author = db.get(Author, id)
    db.delete(author)
    db.commit()
    db.flush()
