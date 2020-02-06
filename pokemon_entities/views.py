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
        short_image_url = 'media/%s'%(str(pokemon_entity.pokemon.picture))
        image_url = request.build_absolute_uri(short_image_url)
        add_pokemon(
            folium_map, pokemon_entity .lat, pokemon_entity .lon,
            pokemon_entity .pokemon, image_url)

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': 'media/%s'%(pokemon.picture),
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):


    pokemon_type = Pokemon.objects.get(pk=pokemon_id)
    pokemon = {
        'img_url': 'http://127.0.0.1:8000/media/%s'%(pokemon_type.picture),
        'title_ru': pokemon_type.title,
        'description': pokemon_type.description,
        'title_en': pokemon_type.title_en,
        'title_jp': pokemon_type.title_jp,
    }
    requested_pokemons = PokemonEntity.objects.filter(pokemon=pokemon_type)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemons:
        short_image_url = 'http://127.0.0.1:8000/media/%s' % (str(pokemon_entity.pokemon.picture))
        image_url = request.build_absolute_uri(short_image_url)
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon, image_url)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
