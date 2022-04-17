from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from dependencies.DatabaseConnection import get_db_connection
from models.AuthorModel import Author
from schemas.AuthorSchema import AuthorSchema

class AuthorRepository:
  db: Session
  
  def __init__(self, db: Session = Depends(get_db_connection)) -> None:
    self.db = db

  def list(self, limit: int, start: int) -> List[AuthorSchema]:
    return [author.__dict__ for author in self.db.query(Author).offset(start).limit(limit).all()]

  def get(self, id: int) -> AuthorSchema:
    return self.db.get(Author, id).__dict__

  def create(self, body: AuthorSchema) -> AuthorSchema:
    author = Author(name=body.name)
    self.db.add(author)
    self.db.commit()
    self.db.refresh(author)
    return author.__dict__

  def update(self, id: int, body: AuthorSchema) -> AuthorSchema:
    author = self.db.get(Author, id)
    author.name = body.name
    self.db.commit()
    self.db.refresh(author)
    return author.__dict__

  def delete(self, id: int) -> None:
    author = self.db.get(Author, id)
    self.db.delete(author)
    self.db.commit()
    self.db.flush()
