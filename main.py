from fastapi import FastAPI

from configs.Environment import getEnvironmentVariables
from models.BaseModel import init
from routers.AuthorRouter import AuthorRouter
from routers.BookRouter import BookRouter

# Application Environment Configuration
env = getEnvironmentVariables()

# Core Application Instance
app = FastAPI(
  title=env.APP_NAME,
  version=env.API_VERSION
)

# Add Routers
app.include_router(AuthorRouter)
app.include_router(BookRouter)

# Initialise Data Model Attributes
init()
