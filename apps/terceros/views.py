from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from django.core.paginator import InvalidPage
from django.http import Http404, HttpResponse
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from http import cookies

from django.core.cache import cache

from .models import (
    TipoPersona, Tercero, Persona,
)
from .forms import (
    TipoPersonaForm, TerceroForm,
    PersonaForm,
)
from django.views.generic import (
    View, TemplateView, ListView,
    UpdateView, CreateView, DeleteView
)
from django.urls import reverse_lazy




# TIPO DE PERSONA
class TipoPersonaIndex(ListView):
    template_name = 'terceros/tipopersona/tipopersona_index.html'
    model = TipoPersona
    paginate_by = 7
    context_object_name = 'tipopersonas'


class TipoPersonaCreate(CreateView):
    model = TipoPersona
    template_name = 'terceros/tipopersona/tipopersona_create.html'
    form_class = TipoPersonaForm
    success_url = reverse_lazy('terceros:tipopersona-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Persona|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Persona'
        return context


class TipoPersonaEdit(UpdateView):
    model = TipoPersona
    template_name = 'terceros/tipopersona/tipopersona_create.html'
    form_class = TipoPersonaForm
    success_url = reverse_lazy('terceros:tipopersona-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Persona|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Persona'
        return context


def tipopersona_delete(request, id):
    tipopersona = TipoPersona.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Persona',
            'titulo': 'Tipo de Persona|Eliminar',
            'ruta': 'terceros:tipopersona-index',
            'objeto': tipopersona,
        }
        return render(request, 'terceros/tipopersona/tipopersona_delete.html', contexto)
    else:
        try:
            tipopersona.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Persona, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Persona eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Persona',
            'mensaje': mensaje,
            'titulo': 'Tipo de Persona|Eliminar',
            'ruta': 'terceros:tipopersona-index',
            'objeto': tipopersona.descripcion,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TERCERO
class TerceroIndex(ListView):
    template_name = 'terceros/tercero/tercero_index.html'
    paginate_by = None
    context_object_name = 'terceros'
    
   
    def get_queryset(self):       
        if not self.request.session.get('tercero_index_page_size'):
            self.request.session['tercero_index_page_size'] = 10

        if not self.request.session.get('tercero_index_kword'):
            self.request.session['tercero_index_kword'] = ''
        
        if not self.request.session.get('tercero_index_ascdesc'):
            self.request.session['tercero_index_ascdesc'] = 'asc'

        if not self.request.session.get('tercero_index_orderby'):
            self.request.session['tercero_index_orderby'] = 'nombre'

        if self.request.method == 'GET' and 'tercero_index_kword' in self.request.GET:
            self.request.session['tercero_index_kword'] = self.request.GET.get('tercero_index_kword').lower()
        
        if self.request.method == 'GET' and 'tercero_index_page_size' in self.request.GET:
            self.request.session['tercero_index_page_size'] = int(self.request.GET['tercero_index_page_size'])

        if self.request.method == 'GET' and 'tercero_index_orderby' in self.request.GET:
            self.request.session['tercero_index_orderby'] = self.request.GET['tercero_index_orderby']

        if self.request.method == 'GET' and 'tercero_index_ascdesc' in self.request.GET:
            self.request.session['tercero_index_ascdesc'] = self.request.GET['tercero_index_ascdesc']


        palabra_clave = self.request.session['tercero_index_kword']
        orderby = self.request.session['tercero_index_orderby'].lower()
        ascdesc = self.request.session['tercero_index_ascdesc'].lower()
        page_size = self.request.session['tercero_index_page_size']

        print(palabra_clave)
        print(orderby)
        print(ascdesc)

        self.paginate_by = page_size
        
        if (palabra_clave):
            terceros = Tercero.objects.buscar_tercero(palabra_clave, orderby, ascdesc)
        else:
            terceros = Tercero.objects.todos_tercero(orderby, ascdesc)
                           
        return terceros
    

class TerceroCreate(CreateView):
    model = Tercero
    template_name = 'terceros/tercero/tercero_create.html'
    form_class = TerceroForm
    success_url = reverse_lazy('terceros:tercero-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tercero|Agregar'
        context['titulo_pagina'] = 'Agregar Tercero'
        return context


class TerceroEdit(UpdateView):
    model = Tercero
    template_name = 'terceros/tercero/tercero_create.html'
    form_class = TerceroForm
    success_url = reverse_lazy('terceros:tercero-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tercero|Editar'
        context['titulo_pagina'] = 'Editar Tercero'
        return context


def tercero_delete(request, id):
    terceros = Tercero.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tercero',
            'titulo': 'Tercero|Eliminar',
            'ruta': 'terceros:tercero-index',
            'objeto': terceros,
        }
        return render(request, 'terceros/tercero/tercero_delete.html', contexto)
    else:
        try:
            if terceros.tipo == 'CL':
                terceros.tipo = 'ER'
                terceros.save()
            else:
                terceros.delete()
        except:
            mensaje = 'No puede eliminar Tercero, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tercero eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tercero',
            'mensaje': mensaje,
            'titulo': 'Tercero|Eliminar',
            'ruta': 'terceros:tercero-index',
            'objeto': terceros.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)
    
    
# PERSONA
class PersonaIndex(ListView):
    template_name = 'terceros/persona/persona_index.html'
    # model = Persona
    paginate_by = 10
    context_object_name = 'personas'
    
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '').lower()
        orderby = self.request.GET.get('orderby', '').lower()
        ascdesc = self.request.GET.get('ascdesc', '').lower()
        # page_size = self.request.GET.get('page_size', '')
        
        if ascdesc == 'desc':
            order = '-' + orderby
        elif ascdesc == 'asc':
            order = orderby
        elif not ascdesc:
            order = 'nombre'
                
        """ if page_size == '':
            page_size = 10
        else:
            page_size = int(page_size) """

        # print(f'{palabra_clave}, {orderby}, {ascdesc}, {order}, {page_size}')

        # self.paginate_by = page_size
        
        if (palabra_clave):
            terceros = Tercero.objects.buscar_tercero(palabra_clave, orderby, ascdesc)
        else:
            # terceros = Tercero.objects.all().select_related('ciudad').select_related('zona').order_by(order)
            terceros = Tercero.objects.todos_tercero(orderby, ascdesc)
            
        return terceros


class PersonaCreate(CreateView):
    model = Persona
    template_name = 'terceros/persona/persona_create.html'
    form_class = PersonaForm
    success_url = reverse_lazy('terceros:persona-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Persona|Agregar'
        context['titulo_pagina'] = 'Agregar Persona'
        return context


class PersonaEdit(UpdateView):
    model = Persona
    template_name = 'terceros/persona/persona_create.html'
    form_class = PersonaForm
    success_url = reverse_lazy('terceros:persona-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Persona|Editar'
        context['titulo_pagina'] = 'Editar Persona'
        return context


def persona_delete(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Persona',
            'titulo': 'Persona|Eliminar',
            'ruta': 'terceros:persona-index',
            'objeto': persona,
        }
        return render(request, 'terceros/persona/persona_delete.html', contexto)
    else:
        try:
            persona.delete()
        except:
            mensaje = 'No puede eliminar Persona, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Persona eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Persona',
            'mensaje': mensaje,
            'titulo': 'Persona|Eliminar',
            'ruta': 'terceros:persona-index',
            'objeto': persona,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)