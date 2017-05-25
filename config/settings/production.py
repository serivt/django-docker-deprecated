import os

from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['*'])

# Database

DATABASES = {
    'default': dj_database_url.config()
}

# Static files (CSS, JavaScript, Images)

ROOT_PATH = os.environ.get('ROOT_PATH', BASE_DIR.ancestor(1))

STATIC_ROOT = '%sstatic/' % ROOT_PATH

STATIC_URL = '/static/'

MEDIA_ROOT = '%smedia/' % ROOT_PATH

MEDIA_URL = '/media/'