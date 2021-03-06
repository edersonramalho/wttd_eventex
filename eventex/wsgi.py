"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from dj_static import Cling #app Wsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventex.settings")

#application = get_wsgi_application()

"""
wsgi entra antes da app django(=get_wsgi_application()),
o Cling adicona os arquivos statics antes da app
"""
application = Cling(get_wsgi_application())
