from django.db import models

class Genre(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.TextField()
    year = models.IntegerField()
    genre = models.ManyToManyField(Genre, blank=True)
    summary = models.TextField(max_length=1000)

    def __str__(self):
        return self.title





