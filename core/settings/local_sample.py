# -*- coding: utf-8 -*-
# Local settings for django_starter_tmpl project core project.
from core.settings.base import *

DEBUG = False
DEBUG_TOOLBAR = False
ALLOWED_HOSTS = []
SITE_URL = '#####'

# ==============================================================================
# Email configuration
# ==============================================================================
EMAIL_HOST = '#####'

DEFAULT_FROM_EMAIL = '#####'
ADMINS = (
    ('admin', '#####'),
)
MAIL_CLIENT = (
    ('client', '#####'),
)
MANAGERS = ADMINS


# ==============================================================================
# Database configuration
# ==============================================================================

DATABASES = {
    'default': {
        'HOST': '#####',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '#####',
        'USER': '#####',
        'PASSWORD': '#####'
    }
}
