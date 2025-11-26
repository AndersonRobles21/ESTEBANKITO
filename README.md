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
```
# BASE DE DATOS

Instalación de Docker en Windows 11

Descargar Docker Desktop:
https://www.docker.com/products/docker-desktop/

Instalar con permisos de administrador.

Asegurarse de habilitar WSL 2:

wsl --install


Reiniciar el sistema.

Abrir Docker Desktop y confirmar que esté funcionando.

Creación del archivo docker-compose.yml
Dentro de la carpeta del proyecto, crear un archivo:
docker-compose.yml

Contenido:
```
services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: proyecto_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data/

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:
```
🏗 3. Construcción y ejecución de los contenedores

En la terminal:

docker compose up -d

db → PostgreSQL estará corriendo en localhost:5432
web → Django se ejecutará en localhost:8000
Ver logs:
docker compose logs -f
Detener:
docker compose down

 Instalación del conector psycopg2

Este paso es obligatorio para conectar Django con PostgreSQL.
Instalar:
pip install psycopg2
Si falla, user:
pip install psycopg2-binary

⚙️ 6. Configuración de la Base de Datos en Django
Editar:
proyecto/settings.py

Cambiar la configuración de DATABASES:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proyecto_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
🧱 7. Aplicar migraciones de Django

Ejecutar:

python manage.py makemigrations
python manage.py migrate
Esto crea todas las tablas:
auth_user
django_admin
migraciones
tablas propias del proyecto

🛠 8. Instalar y usar la extensión PostgreSQL en VS Code

Abrir VS Code

Ir a Extensiones → buscar:

PostgreSQL
Instalar la extensión oficial.
Abrir panel izquierdo → PostgreSQL

Crear conexión:
```
Host: localhost
Port: 5432
User: postgres
Password: postgres
Database: proyecto_db
```
Listo: podrás ver todas las tablas.

📊 9. Ver tablas, datos y ejecutar SQL
Ver tablas

Panel izquierdo → PostgreSQL →
public → tables


Ejemplo:

SELECT * FROM auth_user;


Para tus modelos:

SELECT * FROM app_modelo;
