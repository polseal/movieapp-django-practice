import csv
from django.core.management.base import BaseCommand
from main.models import Genre, Movie

#python manage.py load_movies

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('movies_base.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                genres = row['genre'].split('|')
                movie, created = Movie.objects.get_or_create(
                    title=row['title'],
                    year=row['year'],
                    summary=row['summary']
                )
                for genre_name in genres:
                    genre, _ = Genre.objects.get_or_create(name=genre_name)
                    movie.genre.add(genre)
                movie.save()
        self.stdout.write(self.style.SUCCESS('Sucessfully loaded the data'))

