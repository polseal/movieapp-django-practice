from .settings import *

SECRET_KEY ='placeholder'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movieapp_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost', # localhost if you wanna run some code in the IDE!
        'PORT': 5432,
    }
}
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
