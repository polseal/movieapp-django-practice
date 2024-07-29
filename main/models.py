from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.movie.title}"
    
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    def __str__(self):
        return f"Score by {self.user.username} on {self.movie.title} is {self.rating}"





