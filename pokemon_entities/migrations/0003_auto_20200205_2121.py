# Generated by Django 2.2.5 on 2020-02-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20200205_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappear_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
