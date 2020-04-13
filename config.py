"""App configuration."""
from os import environ, path

import redis

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.Redis(host='localhost', port=6379)