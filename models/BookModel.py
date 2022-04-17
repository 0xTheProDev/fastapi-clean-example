from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Table
from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta

# Many-to-Many Relationship between Books and Authors
association_table = Table('book_author_association', EntityMeta.metadata,
  Column('book_id', ForeignKey('books.id')),
  Column('author_id', ForeignKey('authors.id'))
)

class Book(EntityMeta):
  __tablename__ = "books"

  id = Column(Integer)
  name = Column(String(40), nullable=False)
  authors = relationship("Author", lazy="dynamic", secondary=association_table)

  PrimaryKeyConstraint(id)

  def normalize(self):
    return {
      "id": self.id.__str__(),
      "name": self.name.__str__()
    }

