from django.db import models
from .managers import PaisManager


class Pais(models.Model):
    id = models.BigAutoField(primary_key=True)
    pais = models.CharField(
        verbose_name="Nombre", max_length=50, null=False, blank=False, unique=True)
    iso = models.CharField(max_length=2, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = PaisManager()

    class Meta:
        db_table = "paises"
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ["pais"]
        
    
    def save(self, force_insert=False, force_update=False):
        self.pais = self.pais.capitalize()
        self.iso = self.iso.upper()
        super(Pais, self).save(force_insert, force_update)

    def __str__(self):
        return "%s" % (self.pais)


class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    estado = models.CharField(
        verbose_name="Nombre", max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, default=0, verbose_name="País")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "estados"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["estado", "pais"]
        
    """ 
    def save(self, force_insert=False, force_update=False):
        self.estado = self.estado.upper()
        super(Estado, self).save(force_insert, force_update) """

    def __str__(self):
        return"%s" % (self.estado)

    
class Ciudad(models.Model):
    id = models.BigAutoField(primary_key=True)
    ciudad = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name="Estado")
    created_at = models.DateTimeField("Creado", auto_now=True)
    updated_at = models.DateTimeField("Actualizado", auto_now_add=True)

    class Meta:
        db_table = "ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["ciudad", "estado"]
        
    """ 
    def save(self, force_insert=False, force_update=False):
        self.ciudad = self.ciudad.upper()
        super(Ciudad, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s %s" % (self.ciudad, self.estado)
    
    @property
    def pais(self):
        pais = self.estado.pais
        return pais


class Vendedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    apellido = models.CharField(
        verbose_name="Apellido", max_length=50, null=False, blank=False)
    cedula = models.CharField(verbose_name="Nº de Cédula", max_length=12, null=False, blank=False)
    numero_fiscal = models.CharField(verbose_name="RIF", max_length=10, null=False, blank=False)
    direccion = models.CharField(verbose_name="Dirección", max_length=150, null=False, blank=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, verbose_name="Ciudad")
    telefono = models.CharField(verbose_name="Teléfono(s)", max_length=50, null=False, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=80, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "vendedores"
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ["apellido", "nombre"]
    
    """ 
    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.cedula = self.cedula.upper()
        self.numero_fiscal = self.numero_fiscal.upper()
        self.direccion = self.direccion.upper()
        super(Vendedor, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)


class TipoEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_empresa = models.CharField(verbose_name="Tipo de empresa", max_length=50, null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tipo_empresa"
        verbose_name = "Tipo de empresa"
        verbose_name_plural = "Tipos de empresa"
        ordering = ["tipo_empresa"]
        
    """ 
    def save(self, force_insert=False, force_update=False):
        self.tipo_empresa = self.tipo_empresa.upper()
        self.descripcion = self.descripcion.upper()
        super(TipoEmpresa, self).save(force_insert, force_update) """

    def __str__(self):
        return "%s" % (self.tipo_empresa)
