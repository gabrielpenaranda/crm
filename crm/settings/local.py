from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / get_secret('DB_NAME'),
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'crmdb',
    #    'USER': 'root',
    #    'PASSWORD': '',
    #    'HOST': 'localhost',
    #    'PORT': '3306',
    #}
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'http://localhost/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'http://localhost/media/'
