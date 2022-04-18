from fastapi import FastAPI

from configs.Environment import get_environment_variables
from metadata.Tags import Tags
from models.BaseModel import init
from routers.v1.AuthorRouter import AuthorRouter
from routers.v1.BookRouter import BookRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

# Add Routers
app.include_router(AuthorRouter)
app.include_router(BookRouter)

# Initialise Data Model Attributes
init()
