# -*- coding: utf-8 -*-
from core.settings.base import *

ALLOWED_HOSTS = []
LOCAL_SETTINGS = True
DEBUG = True
DEBUG_TOOLBAR = False

# ==============================================================================
# Database configuration
# ==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# ==============================================================================
# Email configuration
# ==============================================================================
EMAIL_HOST = '#####'
DEFAULT_FROM_EMAIL = 'contact@domain.com'

ADMINS = (
     ('admin', 'contact@domain.com'),
)

MAIL_CLIENT =   (
    ('test mail', 'contact@domain.com'),
)

MANAGERS = ADMINS


# ==============================================================================
# Email backend
# ==============================================================================
if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ==============================================================================
# Debug Toolbar configuration
# ==============================================================================
if DEBUG_TOOLBAR:
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
    INTERNAL_IPS = ('127.0.0.1',)

    # Add in the template timing toolbar
    # INSTALLED_APPS = INSTALLED_APPS + ('template_timings_panel',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    )

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]