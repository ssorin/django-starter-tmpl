# -*- coding: utf-8 -*-
# Local settings for django_starter_tmpl project core project.
from core.settings.base import *

DEBUG = False
DEBUG_TOOLBAR = False
ALLOWED_HOSTS = [{ALLOWED_HOSTS}]
SITE_URL = {SITE_URL}

# ==============================================================================
# Email configuration
# ==============================================================================
EMAIL_HOST = {EMAIL_HOST}

DEFAULT_FROM_EMAIL = {DEFAULT_FROM_EMAIL}
ADMINS = (
    ('admin', {ADMIN_EMAIL}),
)
MAIL_CLIENT = (
    ('client', {CLIENT_EMAIL}),
)
MANAGERS = ADMINS


# ==============================================================================
# Database configuration
# ==============================================================================

DATABASES = {
    'default': {
        'HOST': {DB_HOST},
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': {DB_NAME},
        'USER': {DB_USER},
        'PASSWORD': {DB_PASSWORD}
    }
}
