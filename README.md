# Sistema de Monitoreo de Cultivos Inteligente
Descripción del proyecto

Este proyecto consiste en un sistema modular para la gestión y monitoreo de cultivos, sensores, lecturas y alertas, desarrollado con Django y Django REST Framework (DRF). El objetivo es que cada miembro del equipo desarrolle una aplicación independiente siguiendo buenas prácticas de desarrollo, control de versiones y documentación automática de endpoints mediante Swagger/OpenAPI.

El proyecto permite:

Gestionar cultivos y etapas de crecimiento.
Registrar sensores y sus lecturas.
Filtrar información por rangos de fechas, estados y tipos.
Generar alertas automáticas basadas en condiciones críticas.
Calcular indicadores y estadísticas de cultivos y sensores.

# Se tiene que instalar

Instalar Django
pip install django

Instalar Django REST Framework
pip install djangorestframework

Instalar Django CORS Headers
pip install django-cors-headers

Instalar decouple
pip install python-decouple

Instalara dependencias
pip install -r requirements.txt

# Cultivos 
Este parte es un sistema para gestionar cultivos, incluyendo información sobre nombre, variedad, etapa de crecimiento y fecha de siembra. Se implementó utilizando Django, Django REST Framework y django-filters para facilitar la gestión y filtrado de los datos. Además, cuenta con un panel de administración y documentación de la API usando Swagger y Redoc.


Instalar dependencias:
pip install django djangorestframework django-filter drf-yasg
drf-yasg se usa para la documentación Swagger y Redoc.

# Sensores

# Sistema de Monitoreo de Cultivos Inteligente - App Sensores

## Descripción
La aplicación **Sensores** permite gestionar los sensores instalados en el sistema de monitoreo de cultivos.  
Incluye modelos, filtros y validaciones, y está documentada automáticamente mediante Swagger/OpenAPI.

Esta app forma parte del proyecto modular junto con **Cultivos, Lecturas y Alertas**.

---

## Modelos

### TipoSensor
- `nombre`: Nombre del tipo de sensor.
- `descripcion`: Breve descripción del tipo de sensor.

### Sensor
- `nombre`: Nombre del sensor.
- `tipo`: Relación con TipoSensor.
- `fecha_instalacion`: Fecha en que se instaló el sensor.
- `activo`: Booleano que indica si el sensor está activo o inactivo.

**Validaciones:**
- La fecha de instalación no puede ser futura,limitada a solo 4 digitos.

---
## Documentación de la API
Se puede consultar en:

- Swagger: `/swagger/`
- Redoc: `/redoc/`

---

## Dependencias
```bash
django
djangorestframework
django-filter
drf-yasg
python-decouple
