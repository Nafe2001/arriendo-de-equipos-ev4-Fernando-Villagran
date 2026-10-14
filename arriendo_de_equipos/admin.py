from django.contrib import admin
from .models import Arriendo, Equipo


def formato_pesos(valor):
    return f'${valor:,.0f}'.replace(',', '.')


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'valor_diario_pesos')
    list_filter = ('marca',)
    search_fields = ('nombre', 'marca')

    @admin.display(description='Valor diario', ordering='valor_diario')
    def valor_diario_pesos(self, obj):
        return formato_pesos(obj.valor_diario)


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'nombre_cliente', 'fecha_inicio', 'fecha_termino', 'monto_total_pesos')
    list_filter = ('equipo', 'fecha_inicio')
    search_fields = ('equipo__nombre', 'nombre_cliente')

    @admin.display(description='Monto total', ordering='monto_total')
    def monto_total_pesos(self, obj):
        return formato_pesos(obj.monto_total)
