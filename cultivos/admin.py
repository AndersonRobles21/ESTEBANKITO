from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cultivo

@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'variedad', 'etapa', 'fecha_siembra')
    search_fields = ('nombre', 'variedad')
    list_filter = ('etapa',)
