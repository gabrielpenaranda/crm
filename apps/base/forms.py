from django import forms
from .models import (
    Ciudad, Estado, Pais,
    TipoEmpresa,
    Vendedor,
    )


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ["ciudad", "estado"]
        labels = {
            'ciudad': 'Nombre de la ciudad',
            'estado': 'Estado',
        }
        widgets = {
            'ciudad': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la ciudad',
                    'id': 'ciudad'
                }
            ),
            'estado': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione el estado',
                    'id': 'estado',
                }
            )
        }


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["estado", "pais"]
        labels = {
            'estado': 'Nombre del estado',
            'pais':  'País',
        }
        widgets = {
            'estado': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre del estado',
                    'id': 'estado'
                }
            ),
            'pais': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione país',
                    'id': 'pais'
                }
            )
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ["pais"]
        labels = {
            'pais': 'Nombre del país',
        }
        widgets = {
            'pais': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el nombre del país',
                    'id': 'pais'
                }
            )
        }


class TipoEmpresaForm(forms.ModelForm):
    class Meta:
        model = TipoEmpresa
        fields = ["tipo_empresa", "descripcion"]
        labels = {
            'nombre': 'Tipo de empresa',
            'descripcion': 'Descripción',
        }
        widgets = {
            'tipo_empresa': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tipo de empresa',
                    'id': 'tipo_empresa'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            )
        }


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = [
            "nombre",
            "apellido",
            "cedula",
            "numero_fiscal",
            "direccion",
            "ciudad",
            "telefono",
            "email",
         ]
        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "cedula": "Cédula",
            "numero_fiscal": "Identificador Fiscal",
            "direccion": "Dirección",
            "ciudad": "Ciudad",
            "telefono": "Teléfono(s)",
            "email": "E-mail",
         }
        widgets = {
            "nombre": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre',
                    'id': 'nombre'
                }
            ),
            "apellido": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el apellido',
                    'id': 'apellido'
                }
            ),
            "cedula": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la cédula',
                    'id': 'cedula'
                }
            ),
            "numero_fiscal": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el Identificador Fiscal',
                    'id': 'numero_fiscal'
                }
            ),
            "direccion": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la dirección',
                    'id': 'direccion'
                }
            ),
            "ciudad": forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }
            ),
            "telefono": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s)',
                    'id': 'telefono'
                }
            ),
            "email": forms.EmailInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el e-mail',
                    'id': 'email'
                }
            )
         }