from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'trainers': trainers
    }, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id) # Obtener el pokemon por su ID
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id) # Obtener el entrenador por su ID
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))