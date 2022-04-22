import strawberry
from strawberry.types import Info
from configs.GraphQL import (
    get_AuthorService,
    get_BookService,
)

from schemas.graphql.Author import (
    AuthorMutationSchema,
    AuthorSchema,
)
from schemas.graphql.Book import (
    BookMutationSchema,
    BookSchema,
)


@strawberry.type(description="Mutate all Entity")
class Mutation:
    @strawberry.field(description="Adds a new Author")
    def add_author(
        self, author: AuthorMutationSchema, info: Info
    ) -> AuthorSchema:
        authorService = get_AuthorService(info)
        return authorService.create(author)

    @strawberry.field(
        description="Delets an existing Author"
    )
    def delete_author(
        self, author_id: int, info: Info
    ) -> None:
        authorService = get_AuthorService(info)
        return authorService.delete(author_id)

    @strawberry.field(
        description="Updates an existing Author"
    )
    def update_author(
        self,
        author_id: int,
        author: AuthorMutationSchema,
        info: Info,
    ) -> AuthorSchema:
        authorService = get_AuthorService(info)
        return authorService.update(author_id, author)

    @strawberry.field(description="Add a new Book")
    def add_book(
        self, book: BookMutationSchema, info: Info
    ) -> BookSchema:
        bookService = get_BookService(info)
        return bookService.create(book)

    @strawberry.field(
        description="Deletes an existing Book"
    )
    def delete_book(self, book_id: int, info: Info) -> None:
        bookService = get_BookService(info)
        return bookService.delete(book_id)

    @strawberry.field(
        description="Deletes an existing Book"
    )
    def update_book(
        self,
        book_id: int,
        book: BookMutationSchema,
        info: Info,
    ) -> BookSchema:
        bookService = get_BookService(info)
        return bookService.update(book_id, book)
