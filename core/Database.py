from sqlalchemy import create_engine

from configs.Environment import getEnvironmentVariables

# Runtime Environment Configuration
env = getEnvironmentVariables()

# Generate Database URL
DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

# Create Database Engine
Engine = create_engine(
    DATABASE_URL, echo=env.DEBUG_MODE, future=True
)
