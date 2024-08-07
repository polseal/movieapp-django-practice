import os

import dj_database_url
from .settings import *
#for render.com
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
database_url = os.environ.get("DATABASE_URL")
DATABASES = {'default': dj_database_url.config(default=database_url)}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('access',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'AUTH_HEADER_PREFIX': 'Bearer',
}