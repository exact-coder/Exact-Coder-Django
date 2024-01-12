from pathlib import Path
import os
from os import getenv,path
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


dotenv_file = BASE_DIR / '.env.local'

if path.isfile(dotenv_file):
    load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=#r)&qf*&ehnae32#6w=w^d*n-*34+z^mpg9=7#7n_iizij@si'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost','127.0.0.1','exactcoder.com','www.exactcoder.com','https://www.exactcoder.com'
]


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom App
    'home',
    'accounts',
    'article',
    'services',
    'dashboard',
    'protfolio',

    # Third Party App
    # 'whitenoise.runserver_nostatic',
    'django_cleanup.apps.CleanupConfig',
    "phonenumber_field",
        #ckeditor Apps
    'ckeditor',
    'ckeditor_uploader',
        # AllAuth Apps
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.github',
]

AUTH_USER_MODEL = 'accounts.User'

# # Ckeditor Settings
# CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor'
CKEDITOR_UPLOAD_PATH = "static/media/uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    'admin_user': {
        'toolbar': 'full',
        'removePlugins': 'About,exportpdf',
        'removeButtons': 'About',
        'extraPlugins': ','.join(
            ['codesnippet']
        ),
    },
    'default': {
        'toolbar': 'Basic',
        'removePlugins': 'About,exportpdf',
        'removeButtons': 'About',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # AllAuth Middleware
    # "allauth.account.middleware.AccountMiddleware",

    # Custom Middleware
    'accounts.middleware.RestrictAdminMiddleware',
]

ROOT_URLCONF = 'exactcoder_root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'exactcoder_root.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Email Server (Gmail)
EMAIL_BACKEND ="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True




# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# ===Static file Settings===

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'exactcoder_root/static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Allauth settings
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]