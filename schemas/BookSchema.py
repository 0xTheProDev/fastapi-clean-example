from pydantic import BaseModel


class BookPostRequestSchema(BaseModel):
    name: str


class BookSchema(BookPostRequestSchema):
    id: int


class BookAuthorPostRequestSchema(BaseModel):
    author_id: int
