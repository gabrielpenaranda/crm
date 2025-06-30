from django.contrib import admin
from .models import TipoPersona, Tercero, Persona


@admin.register(Tercero)
class TerceroAdmin(admin.ModelAdmin):
    fields = ('nombre', 'nombre_juridico',
        ('rif', 'nit'),
        ('telefono', 'email', 'web'),
        ('ciudad'),
        'descripcion_actividad',
        ('tipo_empresa'),
        ('vendedor')
    )
    ordering = ['nombre', 'nombre_juridico']
    list_display = ['nombre', 'nombre_juridico', 'rif', 'ciudad']
    list_filter = ['ciudad']
    search_fields = ['nombre', 'rif']
    list_per_page = 10


admin.site.register(TipoPersona)
admin.site.register(Persona)