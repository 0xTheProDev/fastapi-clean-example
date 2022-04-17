# Many-to-Many Relationship between Books and Authors
from sqlalchemy import Column, ForeignKey, Table

from models.BaseModel import EntityMeta


book_author_association = Table(
    "book_author_association",
    EntityMeta.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("author_id", ForeignKey("authors.id")),
)
