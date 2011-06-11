import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nice_lyrics_db.deploy_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
