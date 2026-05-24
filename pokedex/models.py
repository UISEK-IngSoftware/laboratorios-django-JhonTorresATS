from django.db import models

"""Modelos de datos de la app pokedex.
Trainer almacena datos del entrenador y Pokemon almacena datos de cada criatura.
"""

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='trainer_pictures/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pokemon(models.Model):
    """Representa a un Pokémon con atributos físicos, tipo y entrenador asignado."""
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = [
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),
    ]
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6, null=False)
    height = models.DecimalField(decimal_places=4, max_digits=6, null=False)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
    )
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name