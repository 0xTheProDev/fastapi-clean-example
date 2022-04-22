from typing import List, Optional

from fastapi import APIRouter, Depends, status

from schemas.pydantic.AuthorSchema import AuthorSchema
from schemas.pydantic.BookSchema import (
    BookAuthorPostRequestSchema,
    BookPostRequestSchema,
    BookSchema,
)
from services.BookService import BookService

BookRouter = APIRouter(prefix="/v1/books", tags=["book"])


@BookRouter.get("/", response_model=List[BookSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    bookService: BookService = Depends(),
):
    return [
        book.normalize()
        for book in bookService.list(
            name, pageSize, startIndex
        )
    ]


@BookRouter.get("/{id}", response_model=BookSchema)
def get(id: int, bookService: BookService = Depends()):
    return bookService.get(id).normalize()


@BookRouter.post(
    "/",
    response_model=BookSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    book: BookPostRequestSchema,
    bookService: BookService = Depends(),
):
    return bookService.create(book).normalize()


@BookRouter.patch("/{id}", response_model=BookSchema)
def update(
    id: int,
    book: BookPostRequestSchema,
    bookService: BookService = Depends(),
):
    return bookService.update(id, book).normalize()


@BookRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, bookService: BookService = Depends()):
    return bookService.delete(id)


@BookRouter.get(
    "/{id}/authors/", response_model=List[AuthorSchema]
)
def get_authors(
    id: int, bookService: BookService = Depends()
):
    return [
        author.normalize()
        for author in bookService.get_authors(id)
    ]


@BookRouter.post(
    "/{id}/authors/", response_model=List[AuthorSchema]
)
def add_author(
    id: int,
    author: BookAuthorPostRequestSchema,
    bookService: BookService = Depends(),
):
    return [
        author.normalize()
        for author in bookService.add_author(id, author)
    ]


@BookRouter.delete(
    "/{id}/authors/{author_id}",
    response_model=List[AuthorSchema],
)
def remove_author(
    id: int,
    author_id: int,
    bookService: BookService = Depends(),
):
    return [
        author.normalize()
        for author in bookService.remove_author(
            id, author_id
        )
    ]
