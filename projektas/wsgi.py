"""
WSGI config for projektas_uzd_penkta_jurgis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projektas_uzd_penkta_jurgis.settings')

application = get_wsgi_application()
