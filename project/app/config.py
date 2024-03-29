# project/app/config.py


import logging
import os
from functools import lru_cache
from typing import Union

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: Union[str, bool] = os.getenv("TESTING", False)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
