# -*- coding: utf-8 -*-
from configurations import values

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
try:
    from S3 import CallingFormat
    AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
except ImportError:
    # TODO: Fix this where even if in Dev this class is called.
    pass

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# INSTALLED_APPS
# END INSTALLED_APPS

# SECRET KEY
# END SECRET KEY

# django-secure
INSTALLED_APPS += ("djangosecure", )

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
SECURE_FRAME_DENY = values.BooleanValue(True)
SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
SESSION_COOKIE_SECURE = values.BooleanValue(False)
SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
SECURE_SSL_REDIRECT = values.BooleanValue(True)
# end django-secure

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
# END SITE CONFIGURATION

INSTALLED_APPS += ("gunicorn", )

# STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
)

