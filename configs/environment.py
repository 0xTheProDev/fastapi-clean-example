from functools import lru_cache
from pydantic import BaseSettings

class EnvironmentSettings(BaseSettings):
  API_VERSION: str
  APP_NAME: str
  DATABASE_DIALECT: str
  DATABASE_HOSTNAME: str
  DATABASE_NAME: str
  DATABASE_PASSWORD: str
  DATABASE_PORT: int
  DATABASE_USERNAME: str
  DEBUG_MODE: bool

  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"


@lru_cache
def getEnvironmentVariables():
  return EnvironmentSettings()
