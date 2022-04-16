from fastapi import FastAPI

from configs.Environment import getEnvironmentVariables
from models.BaseModel import init
from routers.Author import AuthorRouter

# Application Environment Configuration
env = getEnvironmentVariables()

# Core Application Instance
app = FastAPI(
  title=env.APP_NAME
)

# Add Routers
app.include_router(AuthorRouter)

# Initialise Data Model Attributes
init()
