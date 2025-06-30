from django import forms
from .models import (
    TipoPersona, Tercero, Persona,
)


class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = ["descripcion"]
        labels = {
            'descripcion': 'Tipo de persona',
        }
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el tipo de persona',
                    'id': 'descripcion'
                }
            )
        }


class TerceroForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = ["tipo", "nombre", "nombre_juridico", "direccion", "rif", "telefono", "email", 'web', "ciudad", "descripcion_actividad", "tipo_empresa", "vendedor"]
        labels = {
            "tipo": 'Clasificación',
            'nombre': 'Nombre',
            'nombre_juridico': 'Nombre Jurídico',
            'direccion': 'Dirección',
            'rif': 'RIF',
            'telefono': 'Teléfono(s)',
            'email': 'Email',
            'web': 'Sitio web',
            'ciudad': 'Ciudad',
            # 'actividad': 'Actividad',
            # 'ramo': 'Ramo',
            'descripcion_actividad': 'Descripción de la actividad',
            'tamano_empresa': 'Tamaño de la empresa',
            'tipo_empresa': 'Tipo de empresa',
        }
        widgets = {
            'tipo': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2 fs-7',
                    'placeholder': 'Agregue la clasificación',
                    'id': 'tipo'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2 fs-7',
                    'placeholder': 'Ingrese el nombre del tercero',
                    'id': 'nombre'
                }
            ),
            'nombre_juridico': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2 fs-7',
                    'placeholder': 'Ingrese el nombre jurídico del tercero',
                    'id': 'nombre_juridico'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2 fs-7',
                    'placeholder': 'Ingrese la dirección del tercero',
                    'id': 'direccion'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2 fs-7',
                    'placeholder': 'Ingrese el(los) teléfono(s)',
                    'id': 'telefono'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2 fs-7',
                    'placeholder': 'Ingrese el email',
                    'id': 'email'
                }
            ),
            'rif': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2 fs-7',
                    'placeholder': 'Ingrese el RIF',
                    'id': 'rif'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2 fs-7',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }
            ),
            'tipo_empresa': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2 fs-7',
                    'placeholder': 'Ingrese la actividad',
                    'id': 'tipo_empresa'
                }
            ),
            'vendedor': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm fs-7',
                    'placeholder': 'Ingrese el vendedor',
                    'id': 'vendedor'
                }
            ),
        }
        

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["nombre", "apellido", "cargo", "telefono_oficina", "telefono_celular", "tercero", "tipopersona"]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cargo': 'Cargo',
            'telefono_oficina': 'Teléfono Oficina',
            'telefono_celular': 'Teléfono Celular',
            'tercero': 'Tercero',
            'tipopersona': 'Tipo de Persona',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) nombre(s) de la persona',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) apellido(s) de la persona',
                    'id': 'apellido'
                }
            ),
            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el cargo',
                    'id': 'cargo'
                }
            ),
            'telefono_oficina': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s) de oficina',
                    'id': 'telefono_oficina'
                }
            ),
            'telefono_celular': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s) celular(es)',
                    'id': 'telefono_celular'
                }
            ),
            'tercero': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Ingrese el tercero relacionado',
                    'id': 'tercero'
                }
            ),
            'tipopersona': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese el tipo de persona',
                    'id': 'tipopersona'
                }
            )
        }