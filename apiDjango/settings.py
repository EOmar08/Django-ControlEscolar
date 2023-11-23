"""
Django settings for apiDjango project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jto3ms%p-rqyr@afwkg=9m39-mqp$)^n6&xo^icq85lil)x&f&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
PORT = 8000


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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


AZURE_AD_CLIENT_ID = '3acebf80-2f2b-4d3b-9858-5e63ec6371bf'
AZURE_AD_CLIENT_SECRET = 'yvZ8Q~kEmWKP5SzSEjXVRUX550j19mg_OrlxMaZL'
AZURE_AD_AUTHORITY = 'https://login.microsoftonline.com/dcec6cc1-cc36-4bdf-a82c-eaddb2de00ea'
AZURE_AD_REDIRECT_URI = 'http://localhost:8000/auth/microsoft/callback'  # Cambia esto según tu configuración





ROOT_URLCONF = 'apiDjango.urls'

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

WSGI_APPLICATION = 'apiDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_control_escolar_kzbs',
        'USER': 'iscs',
        'PASSWORD': 'ENqgNSR2n96vczYCUBiJA1LVhVEVX3Ul',
        'HOST': 'oregon-postgres.render.com',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'db_control_escolar',
#         'USER': 'postgres',
#         'PASSWORD': 'ENqgNSR2n96vczYCUBiJA1LVhVEVX3Ul',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

LOGIN_REDIRECT_URL = '/redireccionarIndex/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'iscs.teschi@outlook.es'
EMAIL_HOST_PASSWORD = 'ejqbpxphbllsqamb'

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 días en segundos
SESSION_COOKIE_NAME = "ISCS_SESSION"
