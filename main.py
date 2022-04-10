from fastapi import FastAPI

from models.BaseModel import init
from routers.Author import AuthorRouter

# Core Application Instance
app = FastAPI()
app.include_router(AuthorRouter)

# Initialise Data Model Attributes
init()
