from django.contrib import admin
from django.urls import path, include
from .views import (
    CiudadIndex, CiudadCreate, CiudadEdit, ciudad_delete,
    EstadoIndex, EstadoCreate, EstadoEdit, estado_delete,
    PaisIndex, PaisCreate, PaisEdit, pais_delete,
    TipoEmpresaIndex, TipoEmpresaCreate, TipoEmpresaEdit, tipoempresa_delete,
    VendedorIndex, VendedorCreate, VendedorEdit, vendedor_delete,
)


app_name = 'base'

urlpatterns = [
    path('ciudad', CiudadIndex.as_view(), name='ciudad-index'),
    path('ciudad/create', CiudadCreate.as_view(), name='ciudad-create'),
    path('ciudad/edit/<int:pk>', CiudadEdit.as_view(), name='ciudad-edit'),
    path('ciudad/delete/<int:id>', ciudad_delete, name='ciudad-delete'),
    #
    path('estado', EstadoIndex.as_view(), name='estado-index'),
    path('estado/create', EstadoCreate.as_view(), name='estado-create'),
    path('estado/edit/<int:pk>', EstadoEdit.as_view(), name='estado-edit'),
    path('estado/delete/<int:id>', estado_delete, name='estado-delete'),
    #
    path('pais', PaisIndex.as_view(), name='pais-index'),
    path('pais/create', PaisCreate.as_view(), name='pais-create'),
    path('pais/edit/<int:pk>', PaisEdit.as_view(), name='pais-edit'),
    path('pais/delete/<int:id>', pais_delete, name='pais-delete'),
    #
    path('tipo_empresa', TipoEmpresaIndex.as_view(), name='tipoempresa-index'),
    path('tipo_empresa/create', TipoEmpresaCreate.as_view(), name='tipoempresa-create'),
    path('tipo_empresa/edit/<int:pk>', TipoEmpresaEdit.as_view(), name='tipoempresa-edit'),
    path('tipo_empresa/delete/<int:id>', tipoempresa_delete, name='tipoempresa-delete'),
    #
    path('vendedor', VendedorIndex.as_view(), name='vendedor-index'),
    path('vendedor/create', VendedorCreate.as_view(), name='vendedor-create'),
    path('vendedor/edit/<int:pk>', VendedorEdit.as_view(), name='vendedor-edit'),
    path('vendedor/delete/<int:id>', vendedor_delete, name='vendedor-delete'),
]
