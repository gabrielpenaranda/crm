from django.shortcuts import render
from .models import (
    TipoGestion, TipoOportunidad, Etapa,
    Oportunidad, Gestion, Documento, Ficha, Captacion
)
from .forms import (
    TipoGestionForm, TipoOportunidadForm, EtapaForm,
    OportunidadForm, GestionForm, DocumentoForm, FichaForm, CaptacionForm
)
from django.views.generic import (
    View, TemplateView, ListView,
    UpdateView, CreateView, DeleteView
)
from django.urls import reverse_lazy


# TIPO DE GESTION
class TipoGestionIndex(ListView):
    template_name = 'crm/tipogestion/tipogestion_index.html'
    model = TipoGestion
    paginate_by = 7
    context_object_name = 'tipogestiones'


class TipoGestionCreate(CreateView):
    model = TipoGestion
    template_name = 'crm/tipogestion/tipogestion_create.html'
    form_class = TipoGestionForm
    success_url = reverse_lazy('crm:tipogestion-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Gestión|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Gestión'
        return context


class TipoGestionEdit(UpdateView):
    model = TipoGestion
    template_name = 'crm/tipogestion/tipogestion_create.html'
    form_class = TipoGestionForm
    success_url = reverse_lazy('crm:tipogestion-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Gestión|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Gestión'
        return context


def tipogestion_delete(request, id):
    tipogestion = TipoGestion.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Gestión',
            'titulo': 'Tipo de Gestión|Eliminar',
            'ruta': 'crm:tipogestion-index',
            'objeto': tipogestion,
        }
        return render(request, 'crm/tipogestion/tipogestion_delete.html',
                       contexto)
    else:
        try:
            tipogestion.delete()
        except:
            mensaje = "No puede eliminar Tipo de Gestion, tiene registros asociados"
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Gestión eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Gestión',
            'mensaje': mensaje,
            'titulo': 'Tipo de Gestión|Eliminar',
            'ruta': 'crm:tipogestion-index',
            'objeto': tipogestion,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TIPO DE OPORTUNIDAD
class TipoOportunidadIndex(ListView):
    template_name = 'crm/tipooportunidad/tipooportunidad_index.html'
    model = TipoOportunidad
    paginate_by = 7
    context_object_name = 'tipooportunidades'


class TipoOportunidadCreate(CreateView):
    model = TipoOportunidad
    template_name = 'crm/tipooportunidad/tipooportunidad_create.html'
    form_class = TipoOportunidadForm
    success_url = reverse_lazy('crm:tipooportunidad-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Oportunidad|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Oportunidad'
        return context


class TipoOportunidadEdit(UpdateView):
    model = TipoOportunidad
    template_name = 'crm/tipooportunidad/tipooportunidad_create.html'
    form_class = TipoOportunidadForm
    success_url = reverse_lazy('crm:tipooportunidad-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Oportunidad|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Oportunidad'
        return context


def tipooportunidad_delete(request, id):
    tipooportunidad = TipoOportunidad.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Oportunidad',
            'titulo': 'Tipo de Oportunidad|Eliminar',
            'ruta': 'crm:tipooportunidad-index',
            'objeto': tipooportunidad,
        }
        return render(request, 'crm/tipooportunidad/tipooportunidad_delete.html', contexto)
    else:
        try:
            tipooportunidad.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Gestion, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Oportunidad eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Oportunidad',
            'mensaje': mensaje,
            'titulo': 'Tipo de Oportunidad|Eliminar',
            'ruta': 'crm:tipooportunidad-index',
            'objeto': tipooportunidad,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# ETAPA
class EtapaIndex(ListView):
    template_name = 'crm/etapa/etapa_index.html'
    model = Etapa
    paginate_by = 7
    context_object_name = 'etapas'


class EtapaCreate(CreateView):
    model = Etapa
    template_name = 'crm/etapa/etapa_create.html'
    form_class = EtapaForm
    success_url = reverse_lazy('crm:etapa-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Etapa|Agregar'
        context['titulo_pagina'] = 'Agregar Etapa'
        return context


class EtapaEdit(UpdateView):
    model = Etapa
    template_name = 'crm/etapa/etapa_create.html'
    form_class = EtapaForm
    success_url = reverse_lazy('crm:etapa-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Etapa|Editar'
        context['titulo_pagina'] = 'Editar Etapa'
        return context


def etapa_delete(request, id):
    etapa = Etapa.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Etapa',
            'titulo': 'Etapa|Eliminar',
            'ruta': 'crm:etapa-index',
            'objeto': etapa,
        }
        return render(request, 'crm/etapa/etapa_delete.html', contexto)
    else:
        try:
            etapa.delete()
        except:
            mensaje = 'No puede eliminar Etapa, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Etapa eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Etapa',
            'mensaje': mensaje,
            'titulo': 'Etapa|Eliminar',
            'ruta': 'crm:etapa-index',
            'objeto': etapa,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# OPORTUNIDAD
class OportunidadIndex(ListView):
    template_name = 'crm/oportunidad/oportunidad_index.html'
    model = Oportunidad
    paginate_by = 7
    context_object_name = 'oportunidades'


class OportunidadCreate(CreateView):
    model = Oportunidad
    template_name = 'crm/oportunidad/oportunidad_create.html'
    form_class = OportunidadForm
    success_url = reverse_lazy('crm:oportunidad-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Oportunidad|Agregar'
        context['titulo_pagina'] = 'Agregar Oportunidad'
        return context


class OportunidadEdit(UpdateView):
    model = Oportunidad
    template_name = 'crm/oportunidad/oportunidad_create.html'
    form_class = OportunidadForm
    success_url = reverse_lazy('crm:oportunidad-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Oportunidad|Editar'
        context['titulo_pagina'] = 'Editar Oportunidad'
        return context


def oportunidad_delete(request, id):
    oportunidad = Oportunidad.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Oportunidad',
            'titulo': 'Oportunidad|Eliminar',
            'ruta': 'crm:oportunidad-index',
            'objeto': oportunidad,
        }
        return render(request, 'crm/oportunidad/oportunidad_delete.html', contexto)
    else:
        try:
            oportunidad.delete()
        except:
            mensaje = 'No puede eliminar Oportunidad, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Oportunidad eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Oportunidad',
            'mensaje': mensaje,
            'titulo': 'Oportunidad|Eliminar',
            'ruta': 'crm:oportunidad-index',
            'objeto': oportunidad,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# GESTION
class GestionIndex(ListView):
    template_name = 'crm/gestion/gestion_index.html'
    model = Gestion
    paginate_by = 7
    context_object_name = 'gestiones'


class GestionCreate(CreateView):
    model = Gestion
    template_name = 'crm/gestion/gestion_create.html'
    form_class = GestionForm
    success_url = reverse_lazy('crm:gestion-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Gestión|Agregar'
        context['titulo_pagina'] = 'Agregar Gestión'
        return context


class GestionEdit(UpdateView):
    model = Gestion
    template_name = 'crm/gestion/gestion_create.html'
    form_class = GestionForm
    success_url = reverse_lazy('crm:gestion-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Gestión|Editar'
        context['titulo_pagina'] = 'Editar Gestión'
        return context


def gestion_delete(request, id):
    gestion = Gestion.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Gestión',
            'titulo': 'Gestión|Eliminar',
            'ruta': 'crm:gestion-index',
            'objeto': gestion,
        }
        return render(request, 'crm/gestion/gestion_delete.html', contexto)
    else:
        try:
            gestion.delete()
        except:
            mensaje = 'No puede eliminar Gestion, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Gestión eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Gestión',
            'mensaje': mensaje,
            'titulo': 'Gestión|Eliminar',
            'ruta': 'crm:gestion-index',
            'objeto': gestion,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# DOCUMENTO
class DocumentoIndex(ListView):
    template_name = 'crm/documento/documento_index.html'
    model = Documento
    paginate_by = 7
    context_object_name = 'documentos'


class DocumentoCreate(CreateView):
    model = Documento
    template_name = 'crm/documento/documento_create.html'
    form_class = DocumentoForm
    success_url = reverse_lazy('crm:documento-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Documento|Agregar'
        context['titulo_pagina'] = 'Agregar Documento'
        return context


class DocumentoEdit(UpdateView):
    model = Documento
    template_name = 'crm/documento/documento_create.html'
    form_class = GestionForm
    success_url = reverse_lazy('crm:documento-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Documento|Editar'
        context['titulo_pagina'] = 'Editar Documento'
        return context


def documento_delete(request, id):
    documento = Gestion.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Documento',
            'titulo': 'Documento|Eliminar',
            'ruta': 'crm:documento-index',
            'objeto': documento,
        }
        return render(request, 'crm/documento/documento_delete.html', contexto)
    else:
        try:
            documento.delete()
        except:
            mensaje = 'No puede eliminar Documento, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Documento eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Documento',
            'mensaje': mensaje,
            'titulo': 'Documento|Eliminar',
            'ruta': 'crm:documento-index',
            'objeto': documento,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# FICHA
class FichaIndex(ListView):
    template_name = 'crm/ficha/ficha_index.html'
    model = Ficha
    paginate_by = 7
    context_object_name = 'fichas'


class FichaCreate(CreateView):
    model = Ficha
    template_name = 'crm/ficha/ficha_create.html'
    form_class = FichaForm
    success_url = reverse_lazy('crm:ficha-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ficha|Agregar'
        context['titulo_pagina'] = 'Agregar Ficha'
        return context


class FichaEdit(UpdateView):
    model = Ficha
    template_name = 'crm/ficha/ficha_create.html'
    form_class = FichaForm
    success_url = reverse_lazy('crm:ficha-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ficha|Editar'
        context['titulo_pagina'] = 'Editar Ficha'
        return context


def ficha_delete(request, id):
    ficha = Ficha.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Ficha',
            'titulo': 'Ficha|Eliminar',
            'ruta': 'crm:ficha-index',
            'objeto': ficha,
        }
        return render(request, 'crm/ficha/ficha_delete.html', contexto)
    else:
        try:
            ficha.delete()
        except:
            mensaje = 'No puede eliminar Ficha, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Ficha eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Ficha',
            'mensaje': mensaje,
            'titulo': 'Ficha|Eliminar',
            'ruta': 'crm:ficha-index',
            'objeto': ficha,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# CAPTACION
class CaptacionIndex(ListView):
    template_name = 'crm/captacion/captacion_index.html'
    model = Captacion
    paginate_by = 7
    context_object_name = 'captaciones'


class CaptacionCreate(CreateView):
    model = Captacion
    template_name = 'crm/captacion/captacion_create.html'
    form_class = CaptacionForm
    success_url = reverse_lazy('crm:captacion-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Captación|Agregar'
        context['titulo_pagina'] = 'Agregar Captación'
        return context


class CaptacionEdit(UpdateView):
    model = Captacion
    template_name = 'crm/captacion/captacion_create.html'
    form_class = CaptacionForm
    success_url = reverse_lazy('crm:captacion-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Captación|Editar'
        context['titulo_pagina'] = 'Editar Captación'
        return context


def captacion_delete(request, id):
    captacion = Captacion.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Captación',
            'titulo': 'Captación|Eliminar',
            'ruta': 'crm:captacion-index',
            'objeto': captacion,
        }
        return render(request, 'crm/captacion/captacion_delete.html', contexto)
    else:
        try:
            captacion.delete()
        except:
            mensaje = 'No puede eliminar Captación, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Captación eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Captación',
            'mensaje': mensaje,
            'titulo': 'Captación|Eliminar',
            'ruta': 'crm:captacion-index',
            'objeto': captacion,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)