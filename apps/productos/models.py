from django.db import models
from ..crm.models import Segmento


class Definicion(models.Model):
    nombre = models.CharField('Nombre', max_length=255, null=False, blank=False)
    aplicacion = models.TextField('Aplicación')
    carateristicas = models.TextField('Caracteristicas')
    segmento_objetivo = models.ForeignKey(Segmento, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'definiciones'
        verbose_name = 'Definición'
        verbose_name_plural = 'Definiciones'
        ordering = ['created_at', 'nombre']

    def __str__(self):
        return (f'{self.name} - {self.created_at}')
    

class Investigacion(models.Model):
    tecnologia = models.CharField('Tecnología analizada', max_length=100, null=False, blank=False)
    licencia_definicion = models.CharField('Tipo de licencia laboratorio', max_length=100, null=False, blank=False)
    licencia_cliente = models.CharField('Tipo de licencia cliente', max_length=200, null=False, blank=False)
    definicion = models.ForeignKey(Definicion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ínvestigaciones'
        verbose_name = 'Investigación'
        verbose_name_plural = 'Investigaciones'
        ordering = ['definicion', 'created_at', 'tecnologia']

    def __str__(self):
        return (f'{self.definicion} - {self.created_at} - {self.tecnologia}')



