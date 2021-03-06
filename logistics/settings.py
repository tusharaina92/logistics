import os
import sys
import dj_database_url,urlparse
import site

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#sys.path.insert(0, '/development/logistics/logistics/')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'templates')),
    os.path.normpath(os.path.join(BASE_DIR, 'templates/report_templates')),
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '81psubnpj4e1u_dg&044x8tvi^dtou_)0zdw^o85546&ep1kpz'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (
    ('admin', 'abishek.verma@nuvoex.com'),
)
#TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['localhost', 'ship.nuvoex.com', 'test.nuvoex.com']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'client',
    'zoning',
    'internal',
    'awb',
    'transit',
    'userlogin',
    'django_tables2',
    'south',
    'djcelery',
    'subdomains',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'subdomains.middleware.SubdomainURLRoutingMiddleware',
)

#SESSION_COOKIE_DOMAIN = '.local'
ROOT_URLCONF = 'logistics.urls'

SUBDOMAIN_URLCONFS = {
    None: 'logistics.urls', # no subdomain, e.g. ``example.com``
    'www': 'logistics.urls',
    'm': 'logistics.urls.mobile',
}

WSGI_APPLICATION = 'logistics.wsgi.application'

import dj_database_url

if not os.environ.has_key('DATABASE_URL'):
    #local
    os.environ['DATABASE_URL'] = 'postgres://nuvoex1:1@localhost/logistics'
    #live
    #os.environ['DATABASE_URL'] = 'postgres://jicbvmwmbwskco:NpD3QXSn26OyyNQfzqpbkbRUqe@ec2-107-20-191-205.compute-1.amazonaws.com/dbd54pl1797ldj'
    #test
    # os.environ['DATABASE_URL'] = 'postgres://idlrtcknznmgcz:3h4JbXCc-uZcyszS_tOyD-dnT2@ec2-54-204-21-178.compute-1.amazonaws.com/d67g2km220h4dc'
DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'logistics',
        # 'USER': 'nuvoex1',
        # 'PASSWORD': '1',
        # 'HOST': '127.0.0.1'
}
# SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'
#
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '/var/run/redis/redis.sock',
#     },
#}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
SITE_ID = 1

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

STATIC_ROOT = os.path.join(os.getcwd(), "staticfiles")

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

AUTH_PROFILE_MODULE = "internal.Employee"

SESSION_SAVE_EVERY_REQUEST = True

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587

INSTALLED_APPS += ('storages', )

# if not DEBUG:
#     key for aws is deleted here and needs to be assigned whenever used for live server
#
#     
#
# BROKER_URL = "redis://localhost:6379/0"
# CELERY_RESULT_BACKEND = "redis"
# CELERY_REDIS_HOST = "localhost"
# CELERY_REDIS_PORT = 6379
# CELERY_REDIS_DB = 0
# CELERY_SEND_TASK_ERROR_EMAILS = True
# CELERYD_LOG_FILE = '/tmp/celery.log'
#
# import djcelery
#
# djcelery.setup_loader()
