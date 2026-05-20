from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6, null=False)
    height = models.DecimalField(decimal_places=4, max_digits=6, null=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name