from django.db import models
from ..base.models import Ciudad, Vendedor, TipoEmpresa
from .managers import TerceroManager


class TipoPersona(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipopersonas"
        verbose_name = "Tipo de persona"
        verbose_name_plural = "Tipo de personas"
        ordering = ["descripcion"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(TipoPersona, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s" % self.descripcion


class Tercero(models.Model):
    
    class ClaseTercero(models.TextChoices):
        PROSPECTO = 'prospecto', 'Prospecto'
        CLIENTE = 'cliente', 'Cliente'
        EROSION = 'erosion', 'Erosión'
               
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre",
                              max_length=70, null=False, blank=True, unique=True)
    nombre_juridico = models.CharField(
        verbose_name="Nombre jurídico", max_length=100, null=False, blank=True, unique=True)
    direccion = models.CharField(
        verbose_name="Dirección", max_length=200, null=False, blank=True)
    rif = models.CharField(
        verbose_name="RIF", max_length=10, null=False, blank=True, unique=True)
    telefono = models.CharField(
        verbose_name="Teléfono(s)", max_length=80, null=False, blank=True)
    email = models.EmailField(verbose_name="E-mail", max_length=250, null=True, blank=True)
    web = models.URLField(verbose_name="Sitio web", max_length=250, null=True, blank=True)
    ciudad = models.ForeignKey(
        Ciudad, on_delete=models.PROTECT, verbose_name="Ciudad", related_name='tercero_ciudad')
    descripcion_actividad = models.TextField(
        verbose_name="Descripción de la actividad", blank=True, null=True)
    tipo_empresa = models.ForeignKey(
        TipoEmpresa, on_delete=models.PROTECT, default=0, verbose_name="Tipo de empresa")
    tipo = models.CharField(max_length=12, choices=ClaseTercero.choices, default=ClaseTercero.PROSPECTO)
    vendedor = models.ForeignKey(
        Vendedor, on_delete=models.PROTECT, verbose_name="Vendedor")
    objects = TerceroManager()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "terceros"
        verbose_name = "Tercero"
        verbose_name_plural = "Terceros"
        ordering = ["nombre"]
        indexes = [
            models.Index(fields=[
                "nombre"
            ]),
        ]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.nombre = self.nombre.upper()
        self.nombre_juridico = self.nombre_juridico.upper()
        self.direccion = self.direccion.upper()
        self.rif = self.rif.upper()
        self.descripcion_actividad = self.descripcion_actividad.upper()
        super(Tercero, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.rif, self.nombre_juridico, self.tipo)


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre",
                              max_length=50, null=False, blank=False)
    apellido = models.CharField(
        verbose_name="Apellido", max_length=50, null=False, blank=False)
    cargo = models.CharField(verbose_name="Cargo",
                             max_length=70, null=False, blank=False)
    telefono_oficina = models.CharField(
        verbose_name="Teléfono(s) de oficina", max_length=70, null=False, blank=False)
    telefono_celular = models.CharField(
        verbose_name="Celular", max_length=70, null=False, blank=False)
    tercero = models.ForeignKey(
        Tercero, on_delete=models.PROTECT, verbose_name="Tercero")
    tipopersona = models.ForeignKey(
        TipoPersona, on_delete=models.PROTECT, verbose_name="Tipo de persona")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.cargo = self.cargo.upper()
        super(Persona, self).save(force_insert, force_update) """

    class Meta:
        db_table = "personas"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ["tercero_id__nombre", "apellido", "nombre", "cargo"]

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)