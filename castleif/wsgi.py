"""
WSGI config for castleif project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'castleif.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
