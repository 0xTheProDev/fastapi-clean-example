from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)

from models.BaseModel import EntityMeta


class Author(EntityMeta):
    __tablename__ = "authors"

    id = Column(Integer)
    name = Column(String(16), nullable=False)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }
