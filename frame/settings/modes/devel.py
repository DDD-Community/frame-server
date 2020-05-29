import os

from frame.settings import SERVER_SOFTWARE
from frame.settings.secrets import load_secrets


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

if SERVER_SOFTWARE == 'Heroku':
    ALLOWED_HOSTS += ['frame-server.herokuapp.com',]

if SERVER_SOFTWARE == '':
    from frame.settings.modes.local import ALLOWED_HOSTS as LOCAL_ALLOWED_HOSTS
    ALLOWED_HOSTS += LOCAL_ALLOWED_HOSTS


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': load_secrets('DATABASE_NAME'),
        'USER': load_secrets('DATABASE_USER'),
        'PASSWORD': load_secrets('DATABASE_PASSWORD'),
        'HOST': load_secrets('DATABASE_HOST'),
        'PORT': load_secrets('DATABASE_PORT'),
    }
}
