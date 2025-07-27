import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinescope.settings')
django.setup()

from movieapp.models import Movie

sample_movies = [
    {
        "title": "Fight Club",
        "description": "An underground fight club that becomes something more.",
        "release_year": 1999,
        "genre": "Action"
    },
    {
        "title": "Inception",
        "description": "A skilled thief enters people's dreams to steal secrets.",
        "release_year": 2010,
        "genre": "Sci-Fi"
    },
    {
        "title": "The Dark Knight",
        "description": "Batman faces the Joker in a battle for Gotham.",
        "release_year": 2008,
        "genre": "Action"
    },
    {
        "title": "Interstellar",
        "description": "A team of explorers travels through a wormhole in space.",
        "release_year": 2014,
        "genre": "Sci-Fi"
    }
]

for movie in sample_movies:
    Movie.objects.get_or_create(**movie)

print("Sample movies added successfully!")
