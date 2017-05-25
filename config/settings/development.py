import os

from .base import *


DEBUG = True

SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = ['*']

# Database

DATABASES_DEFAULT = 'sqlite:////%s' % BASE_DIR.child('db.sqlite3')

DATABASES = {
    'default': dj_database_url.config(default=DATABASES_DEFAULT)
}

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.ancestor(1).child('media')

MEDIA_URL = '/media/'