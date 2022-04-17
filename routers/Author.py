from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional

from dependencies.DatabaseConnection import get_db_connection
from repositories.AuthorRepository import AuthorRepository
from schemas.AuthorSchema import AuthorPostRequestSchema, AuthorPostResponseSchema, AuthorSchema

AuthorRouter = APIRouter(prefix="/authors", tags=["author"])

@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(pageSize: Optional[int] = 100, startIndex: Optional[int] = 0, db: Session = Depends(get_db_connection)):
  return AuthorRepository.get_all(db, pageSize, startIndex)

@AuthorRouter.get("/{id}", response_model=AuthorSchema)
def get(id: int, db: Session = Depends(get_db_connection)):
  return AuthorRepository.get_by_id(db, id)

@AuthorRouter.post("/", response_model=AuthorPostResponseSchema, status_code=status.HTTP_201_CREATED)
def create(author: AuthorPostRequestSchema, db: Session = Depends(get_db_connection)):
  return AuthorRepository.create(db, author)

@AuthorRouter.put("/{id}", response_model=AuthorSchema)
def update(id: int, author: AuthorPostRequestSchema, db: Session = Depends(get_db_connection)):
  return AuthorRepository.update(db, id, author)

@AuthorRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db_connection)):
  return AuthorRepository.delete(db, id)
