from typing import List
import strawberry

from schemas.graphql.Book import BookSchema


@strawberry.type(description="Author Schema")
class AuthorSchema:
    id: int
    name: str
    books: List[BookSchema]


@strawberry.input(description="Author Mutation Schema")
class AuthorMutationSchema:
    name: str
