from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.AuthorSchema import AuthorSchema

from schemas.BookSchema import BookPostRequestSchema, BookPostResponseSchema, BookSchema
from services.BookService import BookService

BookRouter = APIRouter(prefix="/books", tags=["book"])

@BookRouter.get("/", response_model=List[BookSchema])
def index(pageSize: Optional[int] = 100, startIndex: Optional[int] = 0, bookService: BookService = Depends()):
  return bookService.list(pageSize, startIndex)

@BookRouter.get("/{id}", response_model=BookSchema)
def get(id: int, bookService: BookService = Depends()):
  return bookService.get(id)

@BookRouter.post("/", response_model=BookPostResponseSchema, status_code=status.HTTP_201_CREATED)
def create(book: BookPostRequestSchema, bookService: BookService = Depends()):
  return bookService.create(book)

@BookRouter.put("/{id}", response_model=BookSchema)
def update(id: int, book: BookPostRequestSchema, bookService: BookService = Depends()):
  return bookService.update(id, book)

@BookRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, bookService: BookService = Depends()):
  return bookService.delete(id)

@BookRouter.get("/{id}/author", response_model=List[AuthorSchema])
def get_author(id: int, bookService: BookService = Depends()):
  return bookService.get_author(id)
