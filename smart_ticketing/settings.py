from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv(
    "um4f6up20+bpyv&^v83=0%vwbnx@#$i75p=@vk!w$m^9f0f(tk"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
)=="True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]


INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'tickets',
    'dashboard',
    'chatbot',
    'ai',
    'ai_chatbot',
    'knowledge',

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


ROOT_URLCONF = 'smart_ticketing.urls'


TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / "templates"
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]


WSGI_APPLICATION = 'smart_ticketing.wsgi.application'


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'smart_ticketing_db',

        'USER': 'ticket_admin',

        'PASSWORD': 'Lokesh@123',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}



AUTH_PASSWORD_VALIDATORS = []



LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'


STATICFILES_DIRS = [

    BASE_DIR / "static"

]



MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"



LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard"

LOGOUT_REDIRECT_URL = "login"



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.User'