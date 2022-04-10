from fastapi import APIRouter, status
from typing import List, Optional

from models.AuthorModel import Author
from schemas.AuthorSchema import AuthorPostRequestSchema, AuthorPostResponseSchema, AuthorSchema

AuthorRouter = APIRouter(prefix="/authors", tags=["author"])

@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(pageSize: Optional[int] = 100, startIndex: Optional[int] = 0):
  pass

@AuthorRouter.get("/{id}", response_model=AuthorSchema)
def get(id: int):
  pass

@AuthorRouter.post("/", response_model=AuthorPostResponseSchema, status_code=status.HTTP_201_CREATED)
def create(author: AuthorPostRequestSchema):
  pass

@AuthorRouter.put("/{id}", response_model=AuthorSchema, status_code=status.HTTP_205_RESET_CONTENT)
def update(id: int, author: AuthorPostRequestSchema):
  pass

@AuthorRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
  pass
