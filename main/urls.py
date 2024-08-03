from django.urls import path
from .views import get_movies, create_movie, delete_movie

urlpatterns = [
    path('movies/',  get_movies, name='get_movie'),
    path('movies/create', create_movie, name="create_movie"),
    path('movies/<int:identifier>', get_movies, name="movie_details")
    path('movies/delete/<int:pk>/', delete_movie, name='delete_movie') 

]
