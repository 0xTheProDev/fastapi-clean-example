from pydantic import BaseModel


class AuthorPostRequestSchema(BaseModel):
    name: str


class AuthorSchema(AuthorPostRequestSchema):
    id: int
