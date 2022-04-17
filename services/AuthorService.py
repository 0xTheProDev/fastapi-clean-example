from fastapi import Depends
from typing import List, Optional

from repositories.AuthorRepository import AuthorRepository
from schemas.AuthorSchema import AuthorSchema

class AuthorService:
  authorRepository: AuthorRepository

  def __init__(self, authorRepository: AuthorRepository = Depends()) -> None:
    self.authorRepository = authorRepository

  def create(self, author: AuthorSchema) -> AuthorSchema:
    return self.authorRepository.create(author)

  def delete(self, author_id: int) -> None:
    return self.authorRepository.delete(author_id)

  def get(self, author_id: int) -> AuthorSchema:
    return self.authorRepository.get(author_id)

  def list(self, pageSize: Optional[int] = 100, startIndex: Optional[int] = 0) -> List[AuthorSchema]:
    return self.authorRepository.list(pageSize, startIndex)

  def update(self, author_id: int, author: AuthorSchema) -> AuthorSchema:
    return self.authorRepository.update(author_id, author)
