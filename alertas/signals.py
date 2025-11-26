from django.db.models.signals import post_save
from django.dispatch import receiver
from lecturas.models import Lectura
from .models import ReglaAlerta, Alerta


def _eval_condicion(regla, valor):
    cond = (regla.condicion or '').strip()
    # Buscar operador simple
    if '>' in cond:
        return valor > regla.valor_umbral
    if '<' in cond:
        return valor < regla.valor_umbral
    if '=' in cond or '==' in cond:
        return valor == regla.valor_umbral
    # Si no hay operador en condicion, usar valor_umbral por defecto (>)
    return valor > regla.valor_umbral


@receiver(post_save, sender=Lectura)
def crear_alerta_por_lectura(sender, instance, created, **kwargs):
    if not created:
        return

    lect_val = instance.valor
    sensor = instance.sensor

    reglas = ReglaAlerta.objects.all()
    for regla in reglas:
        # aplicar solo reglas para el tipo de sensor si está definida
        if regla.tipo_sensor and sensor.tipo_id != regla.tipo_sensor_id:
            continue

        try:
            if _eval_condicion(regla, lect_val):
                mensaje = f"Regla {regla.nombre} activada para sensor {sensor.nombre}: valor={lect_val} umbral={regla.valor_umbral}"
                Alerta.objects.create(sensor=sensor, regla=regla, mensaje=mensaje)
        except Exception:
            # no detener flujo por errores en evaluación de reglas
            continue
