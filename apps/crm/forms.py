from django import forms
from .models import (
    TipoGestion, TipoOportunidad, Etapa,
    Oportunidad, Gestion, Documento, Ficha, Captacion
)


class TipoGestionForm(forms.ModelForm):
    class Meta:
        model = TipoGestion
        fields = ["descripcion"]
        labels = {
            'descripcion': 'Tipo de gestión',
        }
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el tipo de gestión',
                    'id': 'descripcion'
                }
            )
        }


class TipoOportunidadForm(forms.ModelForm):
    class Meta:
        model = TipoOportunidad
        fields = ["tipo_oportunidad", "descripcion"]
        labels = {
            'tipo_oportunidad': 'Tipo de oportunidad',
            'descripción': 'Descripción',
        }
        widgets = {
            'tipo_oportunidad': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tipo de oportunidad',
                    'id': 'tipo_oportunidad'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese una descripción',
                    'id': 'descripcion'
                }
            )
        }


class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ["etapa", "descripcion", "porcentaje"]
        labels = {
            'etapa': 'Etapa',
            'descripción': 'Descripción',
            'porcentaje': 'Porcentaje',
        }
        widgets = {
            'etapa': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la etapa',
                    'id': 'etapa'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese una descripción',
                    'id': 'descripcion'
                }
            ),
            'porcentaje': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'min': '5',
                    'max': '100',
                    'step': '5',
                    'placeholder': 'Ingrese el porcentaje',
                    'id': 'porcentaje'
                }
            )
        }


class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidad
        fields = ["oportunidad", "notas", "cerrada",
                  "tipooportunidades", "terceros", "etapas"]
        labels = {
            'oportunidad': 'Descripción de la oportunidad',
            'notas': 'Notas',
            'cerrada': 'Cerrada',
            'tipooportunidades': 'Tipo de Oportunidad',
            'terceros': 'Tercero',
            'etapas': 'Etapa',
        }
        widgets = {
            'oportunidad': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la oportunidad',
                    'id': 'oportunidad'
                }
            ),
            'notas': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese notas de la oportunidad',
                    'id': 'notas'
                }
            ),
            'cerrada': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input mb-2',
                    'id': 'cerrada'
                }
            ),
            'tipooportunidades': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione el tipo de oportunidad',
                    'id': 'tipooportunidades'
                }
            ),
            'terceros': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione el tercero',
                    'id': 'terceros'
                }
            ),
            'etapas': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione una etapa',
                    'id': 'etapa'
                }
            )
        }
        
        
class GestionForm(forms.ModelForm):
    class Meta:
        model = Gestion
        fields = ["descripcion", "resultados", "fecha", "terceros", "tipogestiones"]
        labels = {
            'descripcion': 'Descripción',
            'resultados': 'Resultados/Compromisos',
            'fecha': 'Fecha',
            'terceros': 'Tercero',
            'tipogestiones': 'Tipo de gestión',
        }
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la fecha de la gestión',
                    'id': 'fecha'
                }
            ),
            'tipogestiones': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione el tipo de gestión',
                    'id': 'tipogestiones'
                }
            ),
            'terceros': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione el tercero',
                    'id': 'terceros'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la descripción',
                    'id': 'descripcion'
                }
            ),
            'resultados': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese los resultados o compromisos',
                    'id': 'resultados'
                }
            )
        }
        
        
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ["fecha", "fecha_envio", "tipo_documento", "archivo", "oportunidades", "descripcion"]
        labels = {
            'fecha': 'Fecha del documento',
            'fecha_envio': 'Fecha de envío',
            'tipo_documento': 'Tipo de documento',
            'archivo': 'Archivo',
            'oportunidades': 'Oportunidad',
            'descripcion': 'Descripción',
        }
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la fecha del documento',
                    'id': 'fecha'
                }
            ),
            'fecha_envio': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la fecha de envío',
                    'id': 'fecha_envio'
                }
            ),
            'tipo_documento': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione el tipo de documento',
                    'id': 'tipo_documento'
                }
            ),
            'archivo': forms.FileInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Seleccione el archivo',
                    'id': 'archivo'
                }
            ),
            'oportunidades': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione la oportunidad',
                    'id': 'oportunidades'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la descripción',
                    'id': 'descripcion'
                }
            )
        }
        
        
class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ["terceros", "base_instalada", "erps", "dbms", "osystems", "num_usuarios", "notas"]
        labels = {
            'terceros': 'Tercero',
            'base_instalada': 'Base instalada',
            'erps': 'ERP/Sistemas',
            'dbms': 'Bases de datos',
            'osystems': 'Sistemas operativos',
            'num_usuarios': 'Número de usuarios',
            'notas': 'Notas',
        }
        widgets = {
            'terceros': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese el tercero',
                    'id': 'terceros'
                }
            ),
            'base_instalada': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la base instalada',
                    'id': 'base_instalada'
                }
            ),
            'erps': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Agregue los ERP/Sistemas',
                    'id': 'erps'
                }
            ),
            'dbms': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Agregue los gestores de base de datos',
                    'id': 'dbms'
                }
            ),
            'osystems': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Agregue los sistemas operativos',
                    'id': 'osystems'
                }
            ),
            'num_usuarios': forms.NumberInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'min': '0',
                    'max': '50000',
                    'step': '1',
                    'placeholder': 'Ingrese el número de usuarios',
                    'id': 'num_usuarios'
                }
            ),
            'notas': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Agregue las notas correspondientes',
                    'id': 'notas'
                }
            )
        }


class CaptacionForm(forms.ModelForm):
    class Meta:
        model = Captacion
        fields = ["nombre_empresa", "nombre_persona", "direccion", "telefono_empresa", "email", "telefono_persona", "ciudad",
                  "tipo_oportunidad", "gestion"]
        labels = {
            'nombre_empresa': 'Nombre empresa',
            'nombre_persona': 'Nombre persona',
            'direccion': 'Dirección',
            'email': 'Correo electrónico',
            'telefono_empresa': 'Teléfono(s) empresa',
            'telefono_persona': 'Teléfono(s) persona',
            'ciudad': 'Ciudad',
            'tipo_oportunidad': 'Tipo de oportunidad',
            'gestion': 'Gestión',
        }
        widgets = {
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Seleccione la ciudad',
                    'id': 'ciudad'
                }
            ),
           'tipo_oportunidad': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Describa el tipo de oportunidad',
                    'id': 'tipo_oportunidad'
                }
            ),
            'gestion': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Describa la gestión realizada',
                    'id': 'gestion'
                }
            ),
            'nombre_empresa': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la empresa',
                    'id': 'nompre_empresa'
                }
            ),
            'nombre_persona': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la persona',
                    'id': 'nombre_persona'
                }
            ),
            'telefono_empresa': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s) de la empresa',
                    'id': 'telefono_empresa'
                }
            ),
            'telefono_persona': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s) de la persona',
                    'id': 'telefono_persona'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el email',
                    'id': 'email'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la dirección',
                    'id': 'direccion'
                }
            ),
        }