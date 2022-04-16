from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from .BaseModel import Base

class Author(Base):
  __tablename__ = "authors"

  id = Column(Integer)
  name = Column(String(16))

  PrimaryKeyConstraint(id)
