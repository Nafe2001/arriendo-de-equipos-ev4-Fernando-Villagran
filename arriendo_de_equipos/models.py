from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    descripcion = models.TextField(verbose_name='descripción')
    marca = models.CharField(max_length=100, verbose_name='marca')
    valor_diario = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name='valor diario (pesos)',
    )

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Arriendo(models.Model):
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        related_name='arriendos',
        verbose_name='equipo',
    )
    nombre_cliente = models.CharField(max_length=150, verbose_name='nombre del cliente')
    fecha_inicio = models.DateField(verbose_name='fecha de inicio')
    fecha_termino = models.DateField(verbose_name='fecha de término')
    monto_total = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name='monto total (pesos)',
    )

    class Meta:
        verbose_name = 'arriendo'
        verbose_name_plural = 'arriendos'
        ordering = ['-fecha_inicio', 'nombre_cliente']

    def __str__(self):
        return f'{self.equipo} - {self.nombre_cliente} ({self.fecha_inicio})'
