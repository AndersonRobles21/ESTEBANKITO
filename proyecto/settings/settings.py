"""
Django settings for settings project.
"""

from pathlib import Path
from decouple import config

import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: se lee de las variables de entorno vía python-decouple.
# Para evitar errores en desarrollo, proporcionamos un valor por defecto
# (inseguro) que solo debe usarse localmente. En producción **siempre**
# establece `SECRET_KEY` en el entorno o en un archivo `.env` privado.
SECRET_KEY = config('SECRET_KEY', default='insecure-dev-secret-change-me')

# DEBUG se mantiene True por defecto para desarrollo. En producción
# cambia esto vía una variable de entorno o tu configuración de despliegue.
DEBUG = True

ALLOWED_HOSTS = []

# -----------------------------
# INSTALLED_APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',


    

    # Django REST Framework
    'rest_framework',
    'drf_yasg',
    
    # Tus apps
    'cultivos',
    'sensores',
    'lecturas',
    'alertas',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # ← OBLIGATORIO
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # ← OBLIGATORIO
    'django.contrib.messages.middleware.MessageMiddleware',    # ← OBLIGATORIO
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URLS
# -----------------------------
ROOT_URLCONF = 'settings.urls'

# -----------------------------
# TEMPLATES (OBLIGATORIO)
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # opcional
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

# -----------------------------
# BASE DE DATOS
# -----------------------------
# Cambiado para usar PostgreSQL en lugar de SQLite.
# Usamos `python-decouple` (ya importado arriba) para leer las
# variables de entorno desde un archivo `.env` o desde el entorno
# del sistema. Esto permite mantener credenciales fuera del código.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': os.getenv("POSTGRES_HOST", "db"),
        'PORT': os.getenv("POSTGRES_PORT", 5432),
    }
}


# NOTAS:
# - Para desarrollo local crea un archivo `.env` en la carpeta `proyecto/`
#   (no lo subas al control de versiones). Puedes usar el archivo
#   `proyecto/.env.example` creado en este commit como plantilla.
# - Si prefieres usar una sola variable de conexión, puedes usar
#   `dj-database-url` y `config('DATABASE_URL')`, pero aquí se dejó
#   explícito para mayor claridad y control.


# -----------------------------
# CONTRASEÑAS
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -----------------------------
# INTERNACIONALIZACIÓN
# -----------------------------
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# -----------------------------
# ARCHIVOS ESTÁTICOS
# -----------------------------
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
