"""
Script para poblar datos de prueba en la base de datos
Ejecutar: python manage.py shell < populate_data.py
"""

from cultivos.models import Cultivo
from sensores.models import TipoSensor, Sensor
from alertas.models import TipoAlerta, Alerta
from datetime import datetime, timedelta

# Crear tipos de sensores
tipos_sensores = []
tipos = ['Temperatura', 'Humedad', 'pH', 'Presión']
for tipo in tipos:
    ts = TipoSensor.objects.create(
        nombre=tipo,
        descripcion=f'Sensor de {tipo.lower()}'
    )
    tipos_sensores.append(ts)

# Crear cultivos
cultivos_data = [
    {'nombre': 'Tomate', 'variedad': 'Cherry', 'etapa': 'Floración', 'fecha_siembra': datetime.now().date() - timedelta(days=60)},
    {'nombre': 'Lechuga', 'variedad': 'Romana', 'etapa': 'Crecimiento', 'fecha_siembra': datetime.now().date() - timedelta(days=30)},
]
cultivos = []
for data in cultivos_data:
    cultivo = Cultivo.objects.create(**data)
    cultivos.append(cultivo)

# Crear sensores
sensores = []
for i, tipo in enumerate(tipos_sensores):
    sensor = Sensor.objects.create(
        nombre=f'Sensor {tipo.nombre} {i+1}',
        tipo=tipo,
        fecha_instalacion=datetime.now().date() - timedelta(days=90),
        activo=True
    )
    sensores.append(sensor)

# Crear tipos de alertas
tipos_alertas_data = [
    {'nombre': 'Temperatura Alta', 'nivel': 'CRITICO', 'descripcion': 'La temperatura excede el límite seguro'},
    {'nombre': 'Humedad Baja', 'nivel': 'ADVERTENCIA', 'descripcion': 'La humedad está por debajo del nivel óptimo'},
    {'nombre': 'pH Anormal', 'nivel': 'ADVERTENCIA', 'descripcion': 'El pH del suelo es anormal'},
    {'nombre': 'Temperatura Baja', 'nivel': 'ADVERTENCIA', 'descripcion': 'La temperatura está muy baja'},
]
tipos_alertas = []
for data in tipos_alertas_data:
    ta = TipoAlerta.objects.create(**data)
    tipos_alertas.append(ta)

# Crear alertas de prueba
alertas_data = [
    {
        'sensor': sensores[0],
        'cultivo': cultivos[0],
        'tipo_alerta': tipos_alertas[0],
        'descripcion': 'Temperatura detectada a 38°C en el sector de tomates',
        'valor_medido': 38.5,
        'valor_limite': 30.0,
        'estado': 'ACTIVA'
    },
    {
        'sensor': sensores[1],
        'cultivo': cultivos[0],
        'tipo_alerta': tipos_alertas[1],
        'descripcion': 'Humedad muy baja detectada en los tomates',
        'valor_medido': 25.0,
        'valor_limite': 40.0,
        'estado': 'ACTIVA'
    },
    {
        'sensor': sensores[2],
        'cultivo': cultivos[1],
        'tipo_alerta': tipos_alertas[2],
        'descripcion': 'pH fuera del rango óptimo',
        'valor_medido': 7.8,
        'valor_limite': 6.5,
        'estado': 'RESUELTA',
        'fecha_resolucion': datetime.now()
    },
]

for data in alertas_data:
    Alerta.objects.create(**data)

print("✅ Datos de prueba creados exitosamente!")
print(f"   - {len(tipos_sensores)} tipos de sensores")
print(f"   - {len(cultivos)} cultivos")
print(f"   - {len(sensores)} sensores")
print(f"   - {len(tipos_alertas)} tipos de alertas")
print(f"   - {len(alertas_data)} alertas")
