from pydantic import BaseModel

class BookPostRequestSchema(BaseModel):
  name: str

class BookPostResponseSchema(BaseModel):
  id: int

class BookSchema(BookPostRequestSchema, BookPostResponseSchema):
  pass
