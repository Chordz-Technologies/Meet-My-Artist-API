"""
Django settings for MeetMyArtist project.

Generated by 'django-adminartist startproject' using Django 5.0a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0o33+&h9$-e(jzyom-81z@48ih!pnejr1b10+u4(pq+%h!_*lp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.108', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'corsheaders',
          'drf_yasg',
          'adminartist',
          'businesscategories',
          'event',
          'artistcategories',
          'products',
          'subscription',
          'users',
          'transactions',
          'rest_framework',
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
          'corsheaders.middleware.CorsMiddleware',
          'django.middleware.security.SecurityMiddleware',
          'django.contrib.sessions.middleware.SessionMiddleware',
          'django.middleware.common.CommonMiddleware',
          'django.middleware.csrf.CsrfViewMiddleware',
          'django.contrib.auth.middleware.AuthenticationMiddleware',
          'django.contrib.messages.middleware.MessageMiddleware',
          'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MeetMyArtist.urls'

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

WSGI_APPLICATION = 'MeetMyArtist.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
          'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'findmyartist',
                    'USER': 'root',
                    'PASSWORD': '1234',
                    'HOST': 'localhost',
                    'PORT': '3306',
          }
}

# settings.py
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Your existing MEDIA_ROOT and MEDIA_URL configurations
MEDIA_ROOT_CAROUSEL = os.path.join(BASE_DIR, 'carousel_images')
MEDIA_URL_CAROUSEL = "/carousel_images/"

# New configuration for profile photos
MEDIA_ROOT_PROFILE = os.path.join(BASE_DIR, 'profile_photos')
MEDIA_URL_PROFILE = "/profile_photos/"

# New configuration for 10 photos per user
MEDIA_ROOT_MULTIPLE = os.path.join(BASE_DIR, 'multiple_photos')
MEDIA_URL_MULTIPLE = "/multiple_photos/"

# New configuration for event poster
MEDIA_ROOT_EVENT = os.path.join(BASE_DIR, 'event_posters')
MEDIA_URL_EVENT = "/event_posters/"

# New configuration for product photos
MEDIA_ROOT_PRODUCT = os.path.join('product_photos')
MEDIA_URL_PRODUCT = "/product_photos/"

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
