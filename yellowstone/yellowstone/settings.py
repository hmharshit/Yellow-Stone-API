"""
Django settings for yellowstone project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from mongoengine import connect
import configparser

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser(allow_no_value=True)
config.read('%s/developer.cfg' % PROJECT_DIR)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n&wtm!!6ft#3+i+l*t@cccycuubg8%mdy9@$q%@rg_nzavq2kv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('general', 'DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'complaints',
    'stations',
    'suggestion',
    'states',
    'rest_framework',
    'rest_framework_mongoengine',
    'harshit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yellowstone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yellowstone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DB_NAME = config.get('databases', 'NAME')
DB_USER = config.get('databases','USER')
DB_PASSWORD = config.get('databases','PASSWORD')
DB_HOST = config.get('databases','HOST')
DATABASES = {
    'default': {
        'CONN_MAX_AGE': 500,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}

MONGO_DATABASE = config.get('mongodb','NAME')
MONGO_HOST = config.get('mongodb','HOST')
MONGO_PORT = config.get('mongodb','PORT')
MONGO_USER = config.get('mongodb','USER')
MONGO_PASSWORD = config.get('mongodb','PASSWORD')
connect(MONGO_DATABASE,
        host=MONGO_HOST,
        port= int(MONGO_PORT),
        username=MONGO_USER,
        password=MONGO_PASSWORD)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
