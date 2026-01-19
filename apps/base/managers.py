from django.db import models
from django.db.models import Q

class PaisManager(models.Manager):

    def buscar_pais(self, kword, orderby, ascdesc):

        if ascdesc == 'desc':
            order = '-' + orderby
        elif ascdesc == 'asc':
            order = orderby

        resultado = self.filter(
                Q(pais__icontains=kword)
            ).order_by(order)
        
        return resultado
    
    
    def todos_pais(self, orderby, ascdesc):
        
        if ascdesc == 'desc':
            order = '-' + orderby
        elif ascdesc == 'asc':
            order = orderby
        elif not ascdesc:
            order = 'nombre'

        resultado = self.all().order_by(order)
        
        return resultado