from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from models.BaseModel import EntityMeta

class Author(EntityMeta):
  __tablename__ = "authors"

  id = Column(Integer)
  name = Column(String(16), nullable=False)

  PrimaryKeyConstraint(id)
