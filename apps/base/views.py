from django.shortcuts import render, redirect
from .models import (
    Pais, Estado, Ciudad,
    TipoEmpresa,
    Vendedor
)
from .forms import (
    CiudadForm, EstadoForm, PaisForm,
    TipoEmpresaForm,
    VendedorForm,
)
from django.views.generic import (
    View, TemplateView, ListView,
    UpdateView, CreateView, DeleteView
)
from django.urls import reverse_lazy


# CIUDAD
class CiudadIndex(ListView):
    template_name = 'base/ciudad/ciudad_index.html'
    model = Ciudad
    paginate_by = 7
    context_object_name = 'ciudades'


class CiudadCreate(CreateView):
    model = Ciudad
    template_name = 'base/ciudad/ciudad_create.html'
    form_class = CiudadForm
    success_url = reverse_lazy('base:ciudad-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ciudad|Agregar'
        context['titulo_pagina'] = 'Agregar Ciudad'
        return context


class CiudadEdit(UpdateView):
    model = Ciudad
    template_name = 'base/ciudad/ciudad_create.html'
    form_class = CiudadForm
    success_url = reverse_lazy('base:ciudad-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ciudad|Editar'
        context['titulo_pagina'] = 'Editar Ciudad'
        return context


def ciudad_delete(request, id):
    ciudad = Ciudad.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Ciudad',
            'titulo': 'Ciudad|Eliminar',
            'ruta': 'base:ciudad-index',
            'objeto': ciudad,
        }
        return render(request, 'base/ciudad/ciudad_delete.html', contexto)
    else:
        try:
            ciudad.delete()
        except:
            mensaje = 'No puede eliminar Ciudad, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Ciudad eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Ciudad',
            'mensaje': mensaje,
            'titulo': 'Ciudad|Eliminar',
            'ruta': 'base:ciudad-index',
            'objeto': ciudad.ciudad,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# ESTADO
class EstadoIndex(ListView):
    template_name = 'base/estado/estado_index.html'
    model = Estado
    paginate_by = 7
    context_object_name = 'estados'


class EstadoCreate(CreateView):
    model = Estado
    template_name = 'base/estado/estado_create.html'
    form_class = EstadoForm
    success_url = reverse_lazy('base:estado-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Estado|Agregar'
        context['titulo_pagina'] = 'Agregar Estado'
        return context


class EstadoEdit(UpdateView):
    model = Estado
    template_name = 'base/estado/estado_create.html'
    form_class = EstadoForm
    success_url = reverse_lazy('base:estado-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Estado|Editar'
        context['titulo_pagina'] = 'Editar Estado'
        return context


def estado_delete(request, id):
    estado = Estado.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Estado',
            'titulo': 'Estado|Eliminar',
            'ruta': 'base:estado-index',
            'objeto': estado,
        }
        return render(request, 'base/estado/estado_delete.html', contexto)
    else:
        try:
            estado.delete()
        except:
            mensaje = 'No puede eliminar Estado, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Estado eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Estado',
            'mensaje': mensaje,
            'titulo': 'Estado|Eliminar',
            'ruta': 'base:estado-index',
            'objeto': estado.estado,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# PAIS
class PaisIndex(ListView):
    template_name = 'base/pais/pais_index.html'
    model = Pais
    paginate_by = 7
    context_object_name = 'paises'


class PaisCreate(CreateView):
    model = Pais
    template_name = 'base/pais/pais_create.html'
    form_class = PaisForm
    success_url = reverse_lazy('base:pais-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'País|Agregar'
        context['titulo_pagina'] = 'Agregar País'
        return context


class PaisEdit(UpdateView):
    model = Pais
    template_name = 'base/pais/pais_create.html'
    form_class = PaisForm
    success_url = reverse_lazy('base:pais-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'País|Editar'
        context['titulo_pagina'] = 'Editar País'
        return context


def pais_delete(request, id):
    pais = Pais.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar País',
            'titulo': 'País|Eliminar',
            'ruta': 'base:pais-index',
            'objeto': pais,
        }
        return render(request, 'base/pais/pais_delete.html', contexto)
    else:
        try:
            pais.delete()
        except:
            mensaje = 'No puede eliminar País, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'País eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar País',
            'mensaje': mensaje,
            'titulo': 'País|Eliminar',
            'ruta': 'base:pais-index',
            'objeto': pais.pais,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TIPO EMPRESA
class TipoEmpresaIndex(ListView):
    template_name = 'base/tipoempresa/tipoempresa_index.html'
    model = TipoEmpresa
    paginate_by = 7
    context_object_name = 'tipoempresas'


class TipoEmpresaCreate(CreateView):
    model = TipoEmpresa
    template_name = 'base/tipoempresa/tipoempresa_create.html'
    form_class = TipoEmpresaForm
    success_url = reverse_lazy('base:tipoempresa-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Empresa|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Empresa'
        return context


class TipoEmpresaEdit(UpdateView):
    model = TipoEmpresa
    template_name = 'base/tipoempresa/tipoempresa_create.html'
    form_class = TipoEmpresaForm
    success_url = reverse_lazy('base:tipoempresa-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Empresa|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Empresa'
        return context


def tipoempresa_delete(request, id):
    tipoempresa = TipoEmpresa.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Empresa',
            'titulo': 'Tipo de Empresa|Eliminar',
            'ruta': 'base:tipoempresa-index',
            'objeto': tipoempresa,
        }
        return render(request, 'base/tipoempresa/tipoempresa_delete.html', contexto)
    else:
        try:
            tipoempresa.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Empresa, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Empresa eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Empresa',
            'mensaje': mensaje,
            'titulo': 'Tipo de Empresa|Eliminar',
            'ruta': 'base:tipoempresa-index',
            'objeto': tipoempresa.tipo_empresa,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# VENDEDOR
class VendedorIndex(ListView):
    template_name = 'base/vendedor/vendedor_index.html'
    model = Vendedor
    paginate_by = 7
    context_object_name = 'vendedores'


class VendedorCreate(CreateView):
    model = Vendedor
    template_name = 'base/vendedor/vendedor_create.html'
    form_class = VendedorForm
    success_url = reverse_lazy('base:vendedor-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Vendedor|Agregar'
        context['titulo_pagina'] = 'Agregar Vendedor'
        return context


class VendedorEdit(UpdateView):
    model = Vendedor
    template_name = 'base/vendedor/vendedor_create.html'
    form_class = VendedorForm
    success_url = reverse_lazy('base:vendedor-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Vendedor|Editar'
        context['titulo_pagina'] = 'Editar Vendedor'
        return context


def vendedor_delete(request, id):
    vendedor = Vendedor.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Vendedor',
            'titulo': 'Vendedor|Eliminar',
            'ruta': 'base:vendedor-index',
            'objeto': vendedor,
        }
        return render(request, 'base/vendedor/vendedor_delete.html', contexto)
    else:
        try:
            vendedor.delete()
        except:
            mensaje = 'No puede eliminar Vendedor, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Vendedor eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Vendedor',
            'mensaje': mensaje,
            'titulo': 'Vendedor|Eliminar',
            'ruta': 'base:vendedor-index',
            'objeto': vendedor.nombre + " " + vendedor.apellido,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)
