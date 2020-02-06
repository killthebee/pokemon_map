from django.db import models

class Pokemon(models.Model):
    title = models.CharField('Русское название покемона', max_length=20)
    title_en = models.TextField('Английское название покемона', max_length=20, null=True, blank=True)
    title_jp = models.TextField('Японское название покемона', null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to='pokemon_pics/')
    description = models.TextField(null=True, blank=True)
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True,)

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

    def __str__(self):
        return '%s, %slvl'%(self.pokemon, self.level)
