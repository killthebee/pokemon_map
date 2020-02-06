import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render

from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons:
        image_url = request.build_absolute_uri(pokemon_entity.pokemon.picture.url)
        add_pokemon(
            folium_map, pokemon_entity .lat, pokemon_entity .lon,
            pokemon_entity .pokemon, image_url)

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.picture.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon_type = Pokemon.objects.get(pk=pokemon_id)
    if pokemon_type.previous_evolution:
        previous_evolution = {
            'pokemon_id': pokemon_type.previous_evolution.id,
            'img_url': pokemon_type.previous_evolution.picture.url,
            'title_ru': pokemon_type.previous_evolution.title,
        }
    else:
        previous_evolution = None

    next_evolution_pokemon = pokemon_type.pokemon_set.first()
    if next_evolution_pokemon:
        next_evolution= {
            'pokemon_id': next_evolution_pokemon.id,
            'img_url': next_evolution_pokemon.picture.url,
            'title_ru': next_evolution_pokemon.title,
        }
    else:
        next_evolution = None

    pokemon = {
        'img_url': pokemon_type.picture.url,
        'title_ru': pokemon_type.title,
        'description': pokemon_type.description,
        'title_en': pokemon_type.title_en,
        'title_jp': pokemon_type.title_jp,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution,
    }

    requested_pokemons = PokemonEntity.objects.filter(pokemon=pokemon_type)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemons:
        image_url = request.build_absolute_uri(pokemon_entity.pokemon.picture.url)
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon, image_url)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
