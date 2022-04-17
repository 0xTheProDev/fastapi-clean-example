from typing import List, Optional

from fastapi import Depends
from models.AuthorModel import Author

from repositories.AuthorRepository import AuthorRepository
from schemas.AuthorSchema import AuthorSchema


class AuthorService:
    authorRepository: AuthorRepository

    def __init__(
        self, authorRepository: AuthorRepository = Depends()
    ) -> None:
        self.authorRepository = authorRepository

    def create(
        self, author_body: AuthorSchema
    ) -> AuthorSchema:
        return self.authorRepository.create(
            Author(name=author_body.name)
        ).normalize()

    def delete(self, author_id: int) -> None:
        return self.authorRepository.delete(
            Author(id=author_id)
        )

    def get(self, author_id: int) -> AuthorSchema:
        return self.authorRepository.get(
            Author(id=author_id)
        ).normalize()

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[AuthorSchema]:
        return [
            author.normalize()
            for author in self.authorRepository.list(
                name, pageSize, startIndex
            )
        ]

    def update(
        self, author_id: int, author_body: AuthorSchema
    ) -> AuthorSchema:
        return self.authorRepository.update(
            author_id, Author(name=author_body.name)
        ).normalize()
