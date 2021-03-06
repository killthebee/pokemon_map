from django.db import models

class Pokemon(models.Model):
    title = models.CharField('Русское название покемона', max_length=20)
    title_en = models.CharField('Английское название покемона', max_length=20, blank=True)
    title_jp = models.CharField('Японское название покемона', max_length=20, blank=True)
    picture = models.ImageField('Картинка', null=True, blank=True, upload_to='pokemon_pics/')
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey("self",
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True,
                                           verbose_name='Покемон-предок',
                                           related_name='next_evolutions')
    element_type = models.ManyToManyField('PokemonElementType', null=True, blank=True, related_name='pokemons')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон', related_name='entities')
    appeared_at = models.DateTimeField('Появиться в', blank=True, default=None, null=True)
    disappear_at = models.DateTimeField('Исчезнет в', blank=True, default=None, null=True)
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)

    def __str__(self):
        return '%s, %slvl'%(self.pokemon, self.level)


class PokemonElementType(models.Model):
    title = models.CharField('Название стихии', max_length=20)
    picture = models.ImageField('Картинка', null=True, blank=True, upload_to='pokemon_elements/')
    strong_against = models.ManyToManyField('self',
                                          null=True,
                                          blank=True,
                                          related_name='weak_against',
                                          verbose_name='Силён против',
                                          symmetrical=False)

    def __str__(self):
        return self.title