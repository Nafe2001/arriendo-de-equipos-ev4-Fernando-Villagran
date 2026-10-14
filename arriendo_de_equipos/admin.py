from django.contrib import admin
from .models import Arriendo, Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'valor_diario')
    search_fields = ('nombre', 'marca')


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'nombre_cliente', 'fecha_inicio', 'fecha_termino', 'monto_total')
    list_filter = ('fecha_inicio', 'fecha_termino')
    search_fields = ('equipo__nombre', 'nombre_cliente')
