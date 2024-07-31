import csv
from django.core.management.base import BaseCommand
from main.models import Genre

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('genres.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Genre.objects.create(name=row['name'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded genres'))
