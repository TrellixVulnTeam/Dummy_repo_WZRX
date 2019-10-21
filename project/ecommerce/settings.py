"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7lgn6levll$61tcn5jl1#tuzybqneh2=(kw@^12b#$tyr8y52('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'batchbvjti@gmail.com'
EMAIL_HOST_PASSWORD = 'vjti@123b'
EMAIL_PORT = '587'
#EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'contact',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'stripe',
    'checkout',
    'booking',
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', #required for allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#For allauth:
AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

#For offline testing we used static folder outside the BASE _DIR
if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static","static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static","media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR),"static","static"),
        )

#template packs of crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
#for allauth:
SITE_ID = 1

#Configuration settings for allauth---------------------------------------------
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/' #The url(here HOME) where the user is redirected after logging in.

ACCOUNT_AUTHENTICATION_METHOD = 'username_email' #implies both username ans email are valid for login.
ACCOUNT_CONFIRM_EMAIL_ON_GET =False #email verified or not is not checked when he logs/logged in.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL #Anonymous user to be redirected fromm emailverification link.
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL =None #Redirect signed in uers to home page.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_REQUIRED =False #Email not required for signup.
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "mD ecommerce" #default email subject on the verification link email.
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True #when user confirms email,he's automat" logged in.
ACCOUNT_LOGOUT_ON_GET = False #Pompt for asking "ARE you sure to Logout."
ACCOUNT_LOGOUT_REDIRECT_URL ="/" #Where the user is redirected after logging out.

ACCOUNT_SIGNUP_FORM_CLASS =None #Custom field for authentication.
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =False
ACCOUNT_UNIQUE_EMAIL = True #No 2 accounts can have same email.

ACCOUNT_USER_MODEL_EMAIL_FIELD ="email" #"email" is default, if not: we need custom user model for field where the user inputs his email.
ACCOUNT_USER_MODEL_USERNAME_FIELD ="username"

ACCOUNT_USERNAME_MIN_LENGTH = 6
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False #password not shown when typed.
ACCOUNT_PASSWORD_MIN_LENGTH = 6

#stripe

#testkeys
STRIPE_PUBLISHABLE_KEY='pk_test_yKmlZXk05TQsuCzvKBr7uNJs'
STRIPE_SECRET_KEY ='sk_test_TcuxME2xfjNgdYwzKPFrNYtu'

#LIVE KEYS
#STRIPE_PUBLISHABLE_KEY=''
#STRIPE_SECRET_KEY =''
