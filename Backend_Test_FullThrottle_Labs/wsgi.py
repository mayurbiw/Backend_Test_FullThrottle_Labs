"""
WSGI config for Backend_Test_FullThrottle_Labs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend_Test_FullThrottle_Labs.settings')

application = get_wsgi_application()
