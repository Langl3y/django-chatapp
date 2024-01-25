import os
from pathlib import Path

from goatstudio.utils import env as env_utils

BASE_CODE_DIR = Path(__file__).resolve().parent.parent

env_utils.load_env(f'{BASE_CODE_DIR}/.env')

# Load env_utils.py
DEBUG_MODE = env_utils.get_boolean('DEBUG_MODE', 'False')

# Time zone
APPLICATION_TIME_ZONE = os.getenv('APPLICATION_TIME_ZONE', 'UTC')

# DB
DB_HOST = os.getenv('DB_HOST', None)
assert DB_HOST

DB_PORT = os.getenv('DB_PORT', None)
assert DB_PORT

DB_NAME = os.getenv('DB_NAME', None)
assert DB_NAME

DB_USER = os.getenv('DB_USER', None)
assert DB_USER

DB_PASSWORD = os.getenv('DB_PASSWORD', None)
assert DB_PASSWORD

# Redis
REDIS_HOST = os.getenv('REDIS_HOST', None)
assert REDIS_HOST

REDIS_PORT = os.getenv('REDIS_PORT', None)
assert REDIS_PORT

# HOST CONFIG
ALLOWED_HOSTS_CONFIG = env_utils.get_list('ALLOWED_HOSTS', ',', [])

FORCE_SCRIPT_NAME_CONFIG = os.getenv('FORCE_SCRIPT_NAME', '')

STATIC_ROOT_DIR = os.getenv('STATIC_ROOT_DIR')

# CORS
CORS_ALLOWED_ORIGINS = env_utils.get_list('CORS_ALLOWED_ORIGINS', ',', [])
CORS_ALLOW_ALL_ORIGINS = env_utils.get_boolean('CORS_ALLOW_ALL_ORIGINS', 'False')
CORS_ALLOW_CREDENTIALS = env_utils.get_boolean('CORS_ALLOW_CREDENTIALS', 'False')

# JWT
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', None)
assert JWT_SECRET_KEY

# Sentry
SENTRY_DSN = os.getenv('SENTRY_DSN', None)
