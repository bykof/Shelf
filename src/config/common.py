# -*- coding: utf-8 -*-
"""
Django settings for Shelf project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from ConfigParser import SafeConfigParser
import os
import ldap
from os.path import join, dirname

from configurations import Configuration, values
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType

BASE_DIR = dirname(dirname(__file__))
PROJECT_ROOT = dirname(dirname(dirname(__file__)))

config = SafeConfigParser()
config.readfp(open(PROJECT_ROOT + '/secrets.cfg'))


class Common(Configuration):
    # APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',  # Useful template tags:  # 'django.contrib.humanize',  # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'crispy_forms',  # Form layouts
        'avatar',  # for user avatars
        'allauth',  # registration
        'allauth.account',  # registration
        'ldap_sync',  # ldap sync
        'taggit',  # django create easy tags
        'rest_framework'  # rest framework for angular
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'api',
        'users',  # custom users app
        'inventory',
        'booking',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
    # END APP CONFIGURATION

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
    # END LDAP CONFIG

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

    # MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        # Make sure djangosecure.middleware.SecurityMiddleware is listed first
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    # END MIDDLEWARE CONFIGURATION

    # REST FRAMEWORK CONFIGURATION
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }
    # END REST FRAMEWORK CONFIGURATION

    # MIGRATIONS CONFIGURATION
    MIGRATION_MODULES = {
        'sites': 'contrib.sites.migrations'
    }
    # END MIGRATIONS CONFIGURATION

    # DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    # In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = 'CHANGEME!!!'
    # END SECRET CONFIGURATION

    # FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )
    # END FIXTURE CONFIGURATION

    # EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # END EMAIL CONFIGURATION

    # MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('''Michael Bykovski''', 'mbykovski@seibert-media.net'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    # END MANAGER CONFIGURATION

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
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
    # END DATABASE CONFIGURATION

    # CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify (used on heroku) is painful to install on windows.
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }
    # END CACHING

    # GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'America/Los_Angeles'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    # END GENERAL CONFIGURATION

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'allauth.account.context_processors.account',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',  # Your stuff: custom template context processers go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
    CRISPY_TEMPLATE_PACK = 'bootstrap3'
    # END TEMPLATE CONFIGURATION

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION

    # URL Configuration
    ROOT_URLCONF = 'urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'
    # End URL Configuration

    # AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    # Some really nice defaults
    ACCOUNT_AUTHENTICATION_METHOD = 'username'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    # END AUTHENTICATION CONFIGURATION

    # Custom user app defaults
    # Select the correct user model
    AUTH_USER_MODEL = 'users.User'
    LOGIN_REDIRECT_URL = 'users:redirect'
    LOGIN_URL = 'account_login'
    # END Custom user app defaults

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    # END LOGGING CONFIGURATION

    @classmethod
    def post_setup(cls):
        cls.DATABASES['default']['ATOMIC_REQUESTS'] = True
