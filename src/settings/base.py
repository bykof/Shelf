import os
import ldap
from ConfigParser import SafeConfigParser

from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

config = SafeConfigParser()
config.readfp(open(PROJECT_ROOT + '/secrets.cfg'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd8kq_a+c0d30!-2j637zd$_md5f#cwa1d4%-e*kx=$c3!t)u=@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

ADMINS = (
    ('''Michael Bykovski''', 'mbykovski@seibert-media.net'),
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


THIRD_PARTY_APPS = (
    'ldap_sync',  # ldap sync
    'taggit',  # django create easy tags
    'taggit_serializer',  # taggit serializer for rest framework
    'rest_framework',  # rest framework for angular
    'rest_framework.authtoken',  # managing the authtoken for client application
    'corsheaders',  # cors headers middleware
)

LOCAL_APPS = (
    'users',
    'api',
    'booking',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'users.User'

# LDAP SYNC CONFIG
LDAP_SYNC_URI = config.get('ldap-sync', 'server_uri')
LDAP_SYNC_BASE = config.get('ldap-sync', 'sync_base')
LDAP_SYNC_BASE_USER = config.get('ldap-sync', 'base_user')
LDAP_SYNC_BASE_PASS = config.get('ldap-sync', 'password')
LDAP_SYNC_USER_FILTER = '(objectClass=user)'
LDAP_SYNC_USER_ATTRIBUTES = {
    'givenName': 'first_name',
    'sn': 'last_name',
    'cn': 'username',
    'mail': 'email',
}
# END LDAP SYNC CONFIG

# LDAP LOGIN CONFIG
# Baseline configuration.
AUTH_LDAP_SERVER_URI = config.get('ldap-login', 'server_uri')

AUTH_LDAP_BIND_DN = (config.get('ldap-login', 'bind_dn'))
AUTH_LDAP_BIND_PASSWORD = config.get('ldap-login', 'password')
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    config.get('ldap-login', 'user_search'),
    ldap.SCOPE_SUBTREE,
    "(CN=%(user)s)",
)

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    config.get('ldap-login', 'group_search'),
    ldap.SCOPE_SUBTREE,
    "(objectClass=group)",
)

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": config.get('ldap-login', 'user_flags_by_group__is_active'),
    "is_staff": config.get('ldap-login', 'user_flags_by_group__is_staff'),
    "is_superuser": config.get('ldap-login', 'user_flags_by_group__is_superuser'),
}

AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 1000
# END LDAP LOGIN CONFIG

# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    )
}
#  END REST FRAMEWORK CONFIGURATION

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('database', 'db_name'),
        'USER': config.get('database', 'username'),
        'PASSWORD': config.get('database', 'password'),
        'HOST': config.get('database', 'host'),
        'PORT': '5432',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)