import os
from .settings import *

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
database_url = os.environ.get("DATABASE_URL")
DATABASES = {'default': dj_database_url.config(default=database_url)}
#DATABASES['default'] = dj_database_url.parse(database_url)