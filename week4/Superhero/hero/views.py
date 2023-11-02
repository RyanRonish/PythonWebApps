from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

superheroes = [
    {
        'id': 'blackwidow',
        'name': 'Black Widow',
        'image': 'black_widow.jpg',
        'strengths': 'Martial Arts, Spy, Smart',
        'weaknesses': 'Mortal, No Special Abilities',
    },
    {
        'id': 'hulk',
        'name': 'Hulk',
        'image': 'hulk.jpg',
        'strengths': 'Strength, Size, Intelliigent',
        'weaknesses': 'Control, Depression',
    },
    {
        'id': 'ironman',
        'name': 'Iron Man',
        'image': 'iron_man.jpg',
        'strengths': 'Intelligence, Gadgets, Armor',
        'weaknesses': 'No superpowers, vulnerability',
    },
    {
        'id': 'flash',
        'name': 'The Flash',
        'image': 'flash.jpg',
        'strengths': 'Intelligence, Speed, Determination',
        'weaknesses': 'DC, Wears Red',
    },
    {
        'id': 'antman',
        'name': 'Ant Man',
        'image': 'antman.jpg',
        'strengths': 'Intelligence, Gadgets, Armor',
        'weaknesses': 'Small, Paul Rudd plays him',
    },
    # Add more superheroes as needed
]

class HeroListView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        heroes = [{'name': hero['name'], 'image': f"/static/images/{hero['image']}"}
                  for hero in superheroes]
        return {'heroes': heroes}
    

class HeroDetailView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        id = kwargs['id']

        # Find the superhero by name in the 'superheroes' list
        superhero = next((hero for hero in superheroes if hero['id'] == id), None)

        if superhero:
            context = {
                'name': superhero['name'],
                'image': f"/static/images/{superhero['image']}",
                'strengths': superhero['strengths'],
                'weaknesses': superhero['weaknesses'],
            }
        else:
            # Handle the case where the superhero is not found
            context = {
                'name': 'Superhero Not Found',
                'image': '/static/images/placeholder.jpg',  # Provide a placeholder image
                'strengths': 'N/A',
                'weaknesses': 'N/A',
            }

        return context