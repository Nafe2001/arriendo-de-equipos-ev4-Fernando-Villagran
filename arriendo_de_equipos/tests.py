from datetime import date
from decimal import Decimal

from django.test import TestCase

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
