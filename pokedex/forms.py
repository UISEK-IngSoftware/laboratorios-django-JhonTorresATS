from django import forms
from .models import Pokemon, Trainer

"""Formularios basados en modelos para la app pokedex.
Se personaliza el estilo Bootstrap y el selector de fecha del entrenador.
"""

class PokemonForm(forms.ModelForm):
    """Formulario para crear y editar un Pokemon."""

    class Meta:
        model = Pokemon     
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type': 'Tipo', 
            'height': 'Altura',
            'weight': 'Peso',
            'trainer': 'Entrenador',
            'picture': 'Imagen'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'type': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'height': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'trainer': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'picture': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }

class TrainerForm(forms.ModelForm):
    """Formulario para crear y editar un entrenador."""

    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'birth_date': 'Fecha de nacimiento',
            'level': 'Nivel',
            'picture': 'Imagen'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}),
            'level': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'picture': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }