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
DEBUG = True

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
    "django_htmx",
        #ckeditor Apps
    'django_ckeditor_5',
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
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "static/media/uploads/"
CKEDITOR_5_UPLOAD_FILE_TYPES = ['jpeg', 'pdf', 'png']
CKEDITOR_RESTRICT_BY_USER = True
# CKEDITOR_5_CONFIGS  = {
#     'default': {
#         'toolbar': 'Basic',
#         'removePlugins': 'About,exportpdf',
#         'removeButtons': 'About',
#     },
#     'extends': {
#         'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
#         'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
#                     'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
#                     'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
#                     'insertTable',],
#         'removePlugins': 'About,exportpdf',
#         'removeButtons': 'About',
#         'extraPlugins': ','.join(
#             ['codesnippet']
#         ),
#     },
# }

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            # 'tableProperties': {
            #     'borderColors': customColorPalette,
            #     'backgroundColors': customColorPalette
            # },
            # 'tableCellProperties': {
            #     'borderColors': customColorPalette,
            #     'backgroundColors': customColorPalette
            # }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' },
                { 'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4' },
                { 'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5' },
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
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
    
    # Third Party Middleware
    # AllAuth Middleware
    # "allauth.account.middleware.AccountMiddleware",
    # HTMX middleware
    "django_htmx.middleware.HtmxMiddleware",
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