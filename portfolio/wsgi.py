"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Github')

application = get_wsgi_application()
