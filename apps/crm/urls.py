from django.contrib import admin
from django.urls import path, include
from .views import (
    TipoGestionIndex, TipoGestionCreate, TipoGestionEdit, tipogestion_delete,
    TipoOportunidadIndex, TipoOportunidadCreate, TipoOportunidadEdit, tipooportunidad_delete,
    EtapaIndex, EtapaCreate, EtapaEdit, etapa_delete,
    OportunidadIndex, OportunidadCreate, OportunidadEdit, oportunidad_delete,
    GestionIndex, GestionCreate, GestionEdit, gestion_delete,
    DocumentoIndex, DocumentoCreate, DocumentoEdit, documento_delete,
    FichaIndex, FichaCreate, FichaEdit, ficha_delete,
    CaptacionIndex, CaptacionCreate, CaptacionEdit, captacion_delete,
)


app_name = 'crm'

urlpatterns = [
    path('tipogestion', TipoGestionIndex.as_view(), name='tipogestion-index'),
    path('tipogestion/create', TipoGestionCreate.as_view(),
         name='tipogestion-create'),
    path('tipogestion/edit/<int:pk>',
         TipoGestionEdit.as_view(), name='tipogestion-edit'),
    path('tipogestion/delete/<int:id>',
         tipogestion_delete, name='tipogestion-delete'),
    #
    path('tipooportunidad', TipoOportunidadIndex.as_view(),
         name='tipooportunidad-index'),
    path('tipooportunidad/create', TipoOportunidadCreate.as_view(),
         name='tipooportunidad-create'),
    path('tipooportunidad/edit/<int:pk>',
         TipoOportunidadEdit.as_view(), name='tipooportunidad-edit'),
    path('tipooportunidad/delete/<int:id>',
         tipooportunidad_delete, name='tipooportunidad-delete'),
    #
    path('etapa', EtapaIndex.as_view(), name='etapa-index'),
    path('etapa/create', EtapaCreate.as_view(),
         name='etapa-create'),
    path('etapa/edit/<int:pk>',
         EtapaEdit.as_view(), name='etapa-edit'),
    path('etapa/delete/<int:id>',
         etapa_delete, name='etapa-delete'),
    #
    path('oportunidad', OportunidadIndex.as_view(),
         name='oportunidad-index'),
    path('oportunidad/create', OportunidadCreate.as_view(),
         name='oportunidad-create'),
    path('oportunidad/edit/<int:pk>',
         OportunidadEdit.as_view(), name='oportunidad-edit'),
    path('oportunidad/delete/<int:id>',
         oportunidad_delete, name='oportunidad-delete'),
    #
    path('gestion', GestionIndex.as_view(), name='gestion-index'),
    path('gestion/create', GestionCreate.as_view(),
         name='gestion-create'),
    path('gestion/edit/<int:pk>',
         GestionEdit.as_view(), name='gestion-edit'),
    path('gestion/delete/<int:id>',
         gestion_delete, name='gestion-delete'),
    #
    path('documento', DocumentoIndex.as_view(), name='documento-index'),
    path('documento/create', DocumentoCreate.as_view(),
         name='documento-create'),
    path('documento/edit/<int:pk>',
         DocumentoEdit.as_view(), name='documento-edit'),
    path('documento/delete/<int:id>',
         documento_delete, name='documento-delete'),
    #
    path('ficha', FichaIndex.as_view(), name='ficha-index'),
    path('ficha/create', FichaCreate.as_view(),
         name='ficha-create'),
    path('ficha/edit/<int:pk>',
         FichaEdit.as_view(), name='ficha-edit'),
    path('ficha/delete/<int:id>',
         ficha_delete, name='ficha-delete'),
#
    path('ficha', FichaIndex.as_view(), name='ficha-index'),
    path('ficha/create', FichaCreate.as_view(),
         name='ficha-create'),
    path('ficha/edit/<int:pk>',
         FichaEdit.as_view(), name='ficha-edit'),
    path('ficha/delete/<int:id>',
         ficha_delete, name='ficha-delete'),
#
    path('captacion', CaptacionIndex.as_view(), name='captacion-index'),
    path('captacion/create', CaptacionCreate.as_view(),
         name='captacion-create'),
    path('captacion/edit/<int:pk>',
         CaptacionEdit.as_view(), name='captacion-edit'),
    path('captacion/delete/<int:id>',
         captacion_delete, name='captacion-delete'),
]