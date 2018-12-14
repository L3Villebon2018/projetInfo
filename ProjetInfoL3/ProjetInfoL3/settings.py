"""
Django settings for ProjetInfoL3 project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import netifaces



def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list


try:
    import netifaces
    ALLOWED_HOSTS = ["charpaknetwork.api-d.com", "localhost", "127.0.0.1"] + ip_addresses()

except ImportError:
    ALLOWED_HOSTS = ["charpaknetwork.api-d.com", "localhost", "127.0.0.1"]


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-bt@shvj7=*985wz&@d*w^+$kux6et#zaf-an#qtuzpz8py1iz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache' if not DEBUG else os.path.join(BASE_DIR, 'cache'),
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

#ALLOWED_HOSTS = []

LOGOUT_REDIRECT_URL = '/'
# Application definition

INSTALLED_APPS = [
    'charpak.apps.CharpakConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'hijack',
    'hijack_admin',
    'compat',

    'debug_toolbar',
    'cachalot'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'ProjetInfoL3.urls'

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #'DIRS': ['templates'],
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

WSGI_APPLICATION = 'ProjetInfoL3.wsgi.application'


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'logfile': {
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename': BASE_DIR + "/../getbeaned.log",
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'logfile']
    },
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = SITE_ROOT + '/media/'
#STATIC_ROOT = SITE_ROOT + '/static/'



STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static/'),
)


FIXTURE_DIRS = (
    os.path.join(SITE_ROOT, 'fixtures/'),
)

HIJACK_USE_BOOTSTRAP = True
HIJACK_ALLOW_GET_REQUESTS = True

LOGIN_REDIRECT_URL = '/' # TODO: Changer l'URL vers laquelle les utilisateurs sont redirigés au login. Une sorte de *page d'acceuil* serait sympa, a voir :)


# Security
if not DEBUG:

    SECURE_SSL_REDIRECT = False  # Nginx
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'



CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = ''


def show_toolbar(request):
    return not request.is_ajax() and request.user and request.user.username == "admin"


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'cachalot.panels.CachalotPanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'ProjetInfoL3.settings.show_toolbar',
    # Rest of config
}