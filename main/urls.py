from django.urls import path
from .views import get_movies, create_movie, movie_details

urlpatterns = [
    path('movies/',  get_movies, name='get_movie'),
    path('movies/create', create_movie, name="create_movie"),
    path('movies/<int:identifier>', movie_details, name="movie_details")
    #path('movies/<int:identifier>', movie_detail_view, name="movie_details")

]
