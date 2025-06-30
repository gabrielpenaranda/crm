from django.contrib import admin
from .models import Etapa, TipoGestion, TipoOportunidad, Gestion, Oportunidad, Documento, Ficha

# Register your models here.

admin.site.register(Etapa)
admin.site.register(TipoGestion)
admin.site.register(TipoOportunidad)
admin.site.register(Gestion)
admin.site.register(Oportunidad)
admin.site.register(Documento)
admin.site.register(Ficha)
