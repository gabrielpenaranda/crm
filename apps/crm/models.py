from django.db import models

from apps.base.models import Ciudad
from apps.terceros.models import Tercero


class Etapa(models.Model):
    id = models.BigAutoField(primary_key=True)
    etapa = models.CharField(verbose_name="Nombre",
                              max_length=50, null=False, blank=False)
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=100, null=False, blank=False)
    porcentaje = models.IntegerField(
        verbose_name="Porcentaje", null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "etapas"
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
        ordering = ["porcentaje", "etapa"]
        
    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.etapa = self.etapa.upper()
        self.descripcion = self.descripcion.upper()
        super(Etapa, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s %s %s" % (self.porcentaje, self.etapa, self.descripcion)


class TipoGestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipogestiones"
        verbose_name = "Tipo de gestión"
        verbose_name_plural = "Tipos de gestión"
        ordering = ["descripcion"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(TipoGestion, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s" % self.descripcion


class TipoOportunidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_oportunidad = models.CharField(verbose_name="Nombre",
                              max_length=50, null=False, blank=False)
    descripcion = models.TextField(
        verbose_name="Descripción", null=False, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipooportunidades"
        verbose_name = "Tipo de oportunidad"
        verbose_name_plural = "Tipos de oportunidad"
        ordering = ["tipo_oportunidad"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.tipo_oportunidad = self.tipo_oportunidad.upper()
        self.descripcion = self.descripcion.upper()
        super(TipoOportunidad, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s %s" % (self.tipo_oportunidad, self.descripcion)


class Gestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField(
        verbose_name="Descripción", null=False, blank=False)
    resultados = models.TextField(
        verbose_name="Resultados", null=False, blank=True)
    fecha = models.DateField(
        verbose_name="Fecha", auto_now=False, auto_now_add=False, null=True)
    terceros = models.ForeignKey(
        Tercero, on_delete=models.PROTECT, verbose_name="Tercero")
    tipogestiones = models.ForeignKey(
        TipoGestion, on_delete=models.PROTECT, verbose_name="Tipo de gestión")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gestiones"
        verbose_name = "Gestion"
        verbose_name_plural = "Gestiones"
        ordering = ["fecha", "terceros", "descripcion"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.resultados = self.resultados.upper()
        self.descripcion = self.descripcion.upper()
        super(Gestion, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s %s %s %s %s" % (self.fecha, self.terceros, self.descripcion, self.resultados, self.tipogestiones)


class Oportunidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    oportunidad = models.CharField(verbose_name="Nombre",
                              max_length=50, null=False, blank=False)
    fecha_inicio = models.DateField(
        verbose_name="Fecha de inicio", auto_now=True, auto_now_add=False)
    # fecha_cierre = models.DateField(
    #    verbose_name="Fecha de cierre", auto_now=False, auto_now_add=False)
    notas = models.TextField(verbose_name="Notas", null=False, blank=True)
    cerrada = models.BooleanField(
        verbose_name="Cerrada", null=False, blank=False, default=False)
    tipooportunidades = models.ForeignKey(
        TipoOportunidad, on_delete=models.PROTECT, verbose_name="Tipo de oportunidad")
    terceros = models.ForeignKey(
        Tercero, on_delete=models.PROTECT, verbose_name="Tercero")
    etapas = models.ForeignKey(
        Etapa, on_delete=models.PROTECT, verbose_name="Etapa")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "oportunidades"
        verbose_name = "Oportunidad"
        verbose_name_plural = "Oportunidades"
        ordering = ["terceros", "oportunidad"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.oportunidad = self.oportunidad.upper()
        self.descripcion = self.descripcion.upper()
        self.notas = self.notas.upper()
        self.status = self.status.upper()
        super(Oportunidad, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.terceros, self.oportunidad, self.descripcion, self.status, self.tipooportunidades,
                                      self.etapas)


class Documento(models.Model):
    
    class TipoDocumento(models.TextChoices):
        PRESENTACION = "PRESENTACION"
        COTIZACION = "COTIZACIÓN"
        PROPUESTA = "PROPUESTA"
        CONTRATO = "CONTRATO"
        BROCHURE = "BROCHURE"
        CUESTIONARIO = "CUESTIONARIO"
        
       
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField(
        verbose_name="Fecha de documento", auto_now=False, auto_now_add=False)
    fecha_envio = models.DateField(
        verbose_name="Fecha de envío", auto_now=False, auto_now_add=False)
    tipo_documento = models.CharField(verbose_name="Tipo de documento", max_length=20,
                                      choices=TipoDocumento.choices, default=TipoDocumento.COTIZACION)
    archivo = models.FileField(
        verbose_name="Archivo", null=True, blank=True, upload_to='documentos/% Y/% m/% d/')
    oportunidades = models.ForeignKey(
        Oportunidad, on_delete=models.PROTECT, verbose_name="Oportunidad")
    descripcion = models.CharField(
        verbose_name="Descripción", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "documentos"
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["fecha", "fecha_envio", "tipo_documento"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Documento, self).save(force_insert, force_update, ) """

    def __str__(self):
        return "%s %s %s %s" % (self.fecha, self.fecha_envio, self.tipo_documento, self.oportunidades)


class Ficha(models.Model):
    id = models.BigAutoField(primary_key=True)
    terceros = models.OneToOneField(Tercero, on_delete=models.PROTECT)
    base_instalada = models.TextField(
        verbose_name="Base instalada", null=False, blank=False)
    erps = models.TextField(verbose_name="ERP/Sistema",
                            null=False, blank=False)
    dbms = models.TextField(
        verbose_name="Manejador(es) de base de datos", null=False, blank=False)
    osystems = models.TextField(
        verbose_name="Sistemas operativos", null=False, blank=False)
    num_usuarios = models.IntegerField(
        verbose_name="Número de usuarios", null=False, blank=False)
    notas = models.TextField(verbose_name="Notas", null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "fichas"
        verbose_name = "Ficha"
        verbose_name_plural = "Fichas"
        ordering = ["terceros"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.base_instalada = self.base_instalada.upper()
        self.erps = self.erps.upper()
        self.dbms = self.dbms.upper()
        self.osystems = self.osystems.upper()
        self.notas = self.notas.upper()
        super(Ficha, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s" % self.terceros


class Captacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_empresa = models.CharField(verbose_name="Nombre empresa", max_length=80, null=False, blank=True)
    nombre_persona = models.CharField(verbose_name="Nombre persona", max_length=60, null=False, blank=True)
    telefono_persona = models.CharField(verbose_name="Teléfonos", max_length=50, null=False, blank=True)
    telefono_empresa = models.CharField(verbose_name="Teléfonos", max_length=50, null=False, blank=True)
    direccion = models.CharField(verbose_name="Dirección", max_length=200, null=False, blank=True)
    email = models.EmailField(verbose_name="Email", max_length=250, null=False, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, verbose_name="Ciudad")
    tipo_oportunidad = models.TextField(verbose_name="Tipo de oportunidad", null=False, blank=False)
    gestion = models.TextField(verbose_name="Gestión", null=False, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "captaciones"
        verbose_name = "Captación"
        verbose_name_plural = "Captaciones"
        ordering = ["nombre_empresa", "nombre_persona"]

    """ 
    def save(self, force_insert=False, force_update=False, **kwargs):
        self.nombre_empresa = self.nombre_empresa.upper()
        self.nombre_persona = self.nombre_persona.upper()
        self.direccion = self.direccion.upper()
        self.tipo_oportunidad = self.tipo_oportunidad.upper()
        self.gestion = self.gestion.upper()
        super(Captacion, self).save(force_insert, force_update, ) """

    def __str__(self):
        return "%s - %s" % (self.nombre_empresa, self.nombre_persona)
