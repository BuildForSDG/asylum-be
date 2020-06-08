import os

import dj_database_url

from core.aws.conf import *
from . base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = AWS_STATIC_URL
MEDIA_ROOT = AWS_MEDIA_URL

DEFAULT_FILE_STORAGE = AWS_FILE_STORAGE
STATICFILES_STORAGE = AWS_STATICFILES_STORAGE
AWS_ACCESS_KEY_ID = ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME = S3_REGION_NAME
AWS_DEFAULT_ACL = DEFAULT_ACL


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Email settings via Gmail
# https://docs.djangoproject.com/en/2.2/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


# Celery Settings
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

BROKER_URL = os.environ['REDIS_URL']
CELERY_RESULT_BACKEND = os.environ['REDIS_URL']
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
