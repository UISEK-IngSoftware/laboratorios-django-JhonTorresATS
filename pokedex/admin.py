from django.contrib import admin
from .models import Pokemon, Trainer

# Register your models here.
admin.site.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass
