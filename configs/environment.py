from pydantic import BaseSettings

class EnvironmentSettings(BaseSettings):
  DATABASE_DIALECT: str
  DATABASE_HOSTNAME: str
  DATABASE_NAME: str
  DATABASE_PASSWORD: str
  DATABASE_PORT: int
  DATABASE_USERNAME: str
  DEBUG_MODE: bool

  class Config:
    env_file = ".env"
