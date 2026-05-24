from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("update_pokemon/<int:pokemon_id>/", views.update_pokemon, name="update_pokemon"),
    path("update_trainer/<int:trainer_id>/", views.update_trainer, name="update_trainer"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("delete_trainer/<int:trainer_id>/", views.delete_trainer, name="delete_trainer"),

]   