# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from core.settings.base import *

gettext = lambda x: x


# ==================================================================
# DJANGO CMS
# ==================================================================
CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
]
# CMS_PERMISSION = True

# ==================================================================
# THUMBNAIL
# ==================================================================
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# ==============================================================================
# Django Filer
# ==============================================================================
FILER_IMAGE_USE_ICON = 32
FILER_IS_PUBLIC_DEFAULT = True
# FILER_ENABLE_PERMISSIONS=True

# DEFULT_LINK_STYLES = (
#     ("default", "Default"),
# )

# CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
#     ("video", _(u"vidéo")),
# )
#
# FILER_LINK_STYLES = (
#     ("default", _("default")),
#     ("button", _("bouton")),
#     ("video", _(u"vidéo")),
#     ("tel", _(u"Téléphone")),
# )

# ==============================================================================
# CKEDITOR
# ==============================================================================
# CKEDITOR_SETTINGS = {
#     'language': '{{ language }}',
#     'toolbar_CMS': [
#         ['Undo', 'Redo'],
#         ['cmsplugins', '-','ShowBlocks'],
#         ['Format'],
#         ['PasteText', 'PasteFromWord'],
#         ['Maximize', ''],
#         '/',
#         ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat'],
#         ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
#         ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
#         ['Source']
#     ],
#     'toolbar': 'CMS',
#     'skin': 'moono-lisa',
#     'format_tags': 'p;h2;h3;h4;h5'
# }

