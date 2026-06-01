from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

"""Vistas principales de la app pokedex.
Incluye la lista de recursos, detalles y formularios CRUD.
"""
def index(request):
    return render(request, 'index.html')

def pokemon_list(request):
    """lista de pokemons."""
    pokemons = Pokemon.objects.all()
    template = loader.get_template('pokemon_list.html')
    context = {
        'pokemons': pokemons,
    }
    return HttpResponse(template.render(context, request))


def trainer_list(request):
    """lista de entrenadores."""
    trainers = Trainer.objects.all()
    template = loader.get_template('trainer_list.html')
    context = {
        'trainers': trainers
    }
    return HttpResponse(template.render(context, request))


def pokemon(request, pokemon_id):
    """Renderiza los detalles del Pokemon identificado por pokemon_id."""
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


def trainer_details(request, trainer_id):
    """Renderiza los detalles del entrenador identificado por trainer_id."""
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

# Agregar un nuevo pokemon, actualizar un pokemon existente y eliminar un pokemon existente
# (esta función crea el formulario y guarda el pokemon si el POST es válido)
@login_required
def add_pokemon(request):
    """Muestra el formulario para crear un Pokemon y guarda los datos enviados."""
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def update_pokemon(request, pokemon_id):
    """Muestra el formulario de edición para un Pokemon existente."""
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = PokemonForm(instance=pokemon)
    
    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, pokemon_id):
    """Elimina un Pokemon y redirige a la página principal."""
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect("pokedex:index") 

# Vista de agregar entrenador, actualizar entrenador y eliminar entrenador
# (usa TrainerForm, guarda el entrenador si el POST es válido)
def add_trainer(request):
    """Muestra el formulario para crear un entrenador y guarda los datos enviados."""
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = TrainerForm()
    
    return render(request, 'trainer_form.html', {'form': form})

def update_trainer(request, trainer_id):
    """Muestra el formulario de edición para un entrenador existente."""
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = TrainerForm(instance=trainer)
    
    return render(request, 'trainer_form.html', {'form': form})

def delete_trainer(request, trainer_id):
    """Elimina un entrenador y redirige a la página principal."""
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect("pokedex:index")

def CustomLoginView(LoginView):
    """Vista personalizada de inicio de sesión usando LoginView."""
    template_name = 'login_form.html' # Ruta de tu plantilla
    success_url = reverse_lazy('pokedex:index') # Redirige a la página principal después de iniciar sesión exitosamente