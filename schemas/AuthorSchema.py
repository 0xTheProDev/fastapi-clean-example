from pydantic import BaseModel

class AuthorPostRequestSchema(BaseModel):
  name: str

class AuthorPostResponseSchema(BaseModel):
  id: int

class AuthorSchema(AuthorPostRequestSchema, AuthorPostResponseSchema):
  pass
