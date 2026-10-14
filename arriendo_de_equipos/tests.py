from datetime import date
from decimal import Decimal

from django.contrib import admin
from django.test import TestCase

from .admin import ArriendoAdmin, EquipoAdmin, formato_pesos
from .models import Arriendo, Equipo


class EquipoArriendoTests(TestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(
            nombre='Taladro percutor',
            descripcion='Taladro para trabajos de construcción',
            marca='Bosch',
            valor_diario=Decimal('12000'),
        )
        self.arriendo = Arriendo.objects.create(
            equipo=self.equipo,
            nombre_cliente='Camila Rojas',
            fecha_inicio=date(2026, 10, 14),
            fecha_termino=date(2026, 10, 16),
            monto_total=Decimal('24000'),
        )

    def test_equipo_y_arriendo_tienen_nombres_legibles(self):
        self.assertEqual(str(self.equipo), 'Taladro percutor')
        self.assertEqual(
            str(self.arriendo),
            'Taladro percutor - Camila Rojas (2026-10-14)',
        )

    def test_eliminar_equipo_elimina_sus_arriendos(self):
        arriendo_id = self.arriendo.pk

        self.equipo.delete()

        self.assertFalse(Arriendo.objects.filter(pk=arriendo_id).exists())

    def test_panel_muestra_montos_en_pesos_chilenos(self):
        self.assertEqual(formato_pesos(Decimal('12990')), '$12.990')
        self.assertEqual(
            EquipoAdmin(Equipo, admin.site).valor_diario_pesos(self.equipo),
            '$12.000',
        )
        self.assertEqual(
            ArriendoAdmin(Arriendo, admin.site).monto_total_pesos(self.arriendo),
            '$24.000',
        )

    def test_listados_tienen_columnas_filtros_y_busqueda(self):
        equipo_admin = EquipoAdmin(Equipo, admin.site)
        arriendo_admin = ArriendoAdmin(Arriendo, admin.site)

        self.assertGreater(len(equipo_admin.get_list_display(request=None)), 1)
        self.assertTrue(equipo_admin.get_list_filter(request=None))
        self.assertTrue(equipo_admin.get_search_fields(request=None))
        self.assertGreater(len(arriendo_admin.get_list_display(request=None)), 1)
        self.assertTrue(arriendo_admin.get_list_filter(request=None))
        self.assertTrue(arriendo_admin.get_search_fields(request=None))
