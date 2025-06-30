from django.urls import path
from .views import (
    TipoPersonaIndex, TipoPersonaCreate, TipoPersonaEdit, tipopersona_delete,
    TerceroIndex, TerceroCreate, TerceroEdit, tercero_delete,
    PersonaIndex, PersonaCreate, PersonaEdit, persona_delete,
)

app_name = "terceros"

urlpatterns = [
    path('tipopersona', TipoPersonaIndex.as_view(), name='tipopersona-index'),
    path('tipopersona/create', TipoPersonaCreate.as_view(),
         name='tipopersona-create'),
    path('tipopersona/edit/<int:pk>',
         TipoPersonaEdit.as_view(), name='tipopersona-edit'),
    path('tipopersona/delete/<int:id>',
         tipopersona_delete, name='tipopersona-delete'),
    #
    path('tercero', TerceroIndex.as_view(), name='tercero-index'),
    path('tercero/create', TerceroCreate.as_view(),
         name='tercero-create'),
    path('tercero/edit/<int:pk>',
         TerceroEdit.as_view(), name='tercero-edit'),
    path('tercero/delete/<int:id>',
         tercero_delete, name='tercero-delete'),
    #
    path('persona', PersonaIndex.as_view(), name='persona-index'),
    path('persona/create', PersonaCreate.as_view(),
         name='persona-create'),
    path('persona/edit/<int:pk>',
         PersonaEdit.as_view(), name='persona-edit'),
    path('persona/delete/<int:id>',
         persona_delete, name='persona-delete'),
]
