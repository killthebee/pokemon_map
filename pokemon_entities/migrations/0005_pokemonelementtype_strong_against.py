# Generated by Django 2.2.5 on 2020-02-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20200212_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(blank=True, null=True, related_name='weak_against', to='pokemon_entities.PokemonElementType', verbose_name='Силён против'),
        ),
    ]
