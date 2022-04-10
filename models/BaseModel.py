from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from engines.Database import Engine

# Local Session Manager
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

# Base Entity Model Schema
Base = declarative_base()

def init():
  Base.metadata.create_all(bind=Engine)
