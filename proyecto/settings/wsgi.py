"""
WSGI config for proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establecer el módulo de settings de Django
# Nota: 'proyecto.settings.settings' es la ruta completa dentro de tu estructura
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings.settings')

application = get_wsgi_application()
