"""Config file."""
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Basic settings."""

    app_name: str = "Your project name"
    cors_allow_origin: str = "*"
    cors_allow_credentials: bool = True
    cors_allow_methods: str = "GET,HEAD,POST,OPTIONS,PUT,PATCH,DELETE"
    cors_allow_headers: str = (
        "Access-Token,Content-Type,referrer,"
        "Authorization,Cache-Control,X-Requested-With"
    )
    log_path: str = "/tmp/app.log"
    error_log_path: str = "/tmp/app-error.log"

    app_token: str = "s0m3customT0k3n"

    class Config:
        """Env file."""

        env_file = ".env"  # Change this to the desired dotenv file


@lru_cache()
def get_config():
    """Get config."""
    return Settings()
