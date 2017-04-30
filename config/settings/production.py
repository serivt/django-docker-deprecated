import os

from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['*'])

# Database

DATABASES = {
    'default': dj_database_url.config()
}