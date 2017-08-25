# -*- coding: utf-8 -*-
from core.settings.apps import *

try:
    from core.settings.env import ENV

    if ENV == 'dev' or ENV == '' or ENV != 'stage' or ENV != 'prod':
        from core.settings.local_dev import *
    if ENV == 'stage':
        from local_stage import *
    if ENV == 'prod':
        from local_prod import *

except ImportError:
    from core.settings.local_dev import *

