"""
WSGI config for proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Agregar 'proyecto/' al path de Python para que Django encuentre las apps
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / 'proyecto'))

from django.core.wsgi import get_wsgi_application

# Establecer el módulo de settings de Django
# Nota: 'settings' es el archivo settings.py en la raíz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
