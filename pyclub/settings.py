# -*- coding: utf-8 -*-

import os

from decouple import config, Csv

SITE_ID = 1

SITE_NAME = 'PythonClub'

TAG_LINE = 'Lorem Ipsum'

BASE_DIR = os.path.dirname(__file__)

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())

# Application definition

INSTALLED_APPS = (
    'flat',
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd
    'debug_toolbar',
    'django_extensions',
    'social.apps.django_app.default',
    # project
    'pyclub.accounts',
    'pyclub.content',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'pyclub.core.context_processors.site_settings'
            ],
        },
    },
]

ROOT_URLCONF = 'pyclub.urls'

WSGI_APPLICATION = 'pyclub.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

from dj_database_url import parse as db_url
DATABASES = {'default': config('DATABASE_URL', cast=db_url)}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static-root')

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media-root')

# Auth

AUTH_USER_MODEL = 'accounts.User'

SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

LOGIN_URL = '/auth/login/'

LOGOUT_URL = '/auth/logout/'

LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')

SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

GITHUB_AUTH_EXTRA_ARGUMENTS = {'scope': 'user:email'}

# Email

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_PORT = config('EMAIL_PORT', cast=int)

# Dirs

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, '..', 'bower_components'),
)
