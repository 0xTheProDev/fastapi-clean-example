from typing import List, Optional

import strawberry
from strawberry.types import Info
from configs.GraphQL import (
    get_AuthorService,
    get_BookService,
)

from schemas.graphql.Author import AuthorSchema
from schemas.graphql.Book import BookSchema


@strawberry.type(description="Query all entities")
class Query:
    @strawberry.field(description="Get an Author")
    def author(
        self, id: int, info: Info
    ) -> Optional[AuthorSchema]:
        authorService = get_AuthorService(info)
        return authorService.get(id)

    @strawberry.field(description="List all Authors")
    def authors(self, info: Info) -> List[AuthorSchema]:
        authorService = get_AuthorService(info)
        return authorService.list()

    @strawberry.field(description="Get a Book")
    def book(
        self, id: int, info: Info
    ) -> Optional[BookSchema]:
        bookService = get_BookService(info)
        return bookService.get(id)

    @strawberry.field(description="List all Books")
    def books(self, info: Info) -> List[BookSchema]:
        bookService = get_BookService(info)
        return bookService.list()
