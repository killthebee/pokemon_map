from django.db import models

class Pokemon(models.Model):
    title = models.TextField()
    picture = models.ImageField(null=True, blank=True, upload_to='pokemon_pics/')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(blank=True, default=None, null=True)
    disappear_at = models.DateTimeField(blank=True, default=None, null=True)
    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
