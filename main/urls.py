from django.urls import path
from .views import get_movies, create_movie, movie_details, user_info

urlpatterns = [
    path('movies/',  get_movies, name='get_movie'),
    path('movies/create', create_movie, name="create_movie"),
    path('movies/<int:pk>', movie_details, name="movie_details"),
    path('user-info/', user_info, name='user_info'),

]
