from fastapi import Depends
from strawberry.types import Info

from services.AuthorService import AuthorService
from services.BookService import BookService


# GraphQL Dependency Context
async def get_graphql_context(
    authorService: AuthorService = Depends(),
    bookService: BookService = Depends(),
):
    return {
        "authorService": authorService,
        "bookService": bookService,
    }


# Extract AuthorService instance from GraphQL context
def get_AuthorService(info: Info) -> AuthorService:
    return info.context["authorService"]


# Extract BookService instance from GraphQL context
def get_BookService(info: Info) -> BookService:
    return info.context["bookService"]
