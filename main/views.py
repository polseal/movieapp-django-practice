from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from main.publisher import publish_message
from .models import Movie
from .serializer import  MovieSerializer

@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def movie_details(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        publish_message('notifications', 'movies', {'action': 'deleted', 'title': movie.title})
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_movie(request):
    data=request.data
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        movie = serializer.save() 
        publish_message('notifications', 'movies', {'movie': movie.id, 'title': movie.title, 'action': 'created'})
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_info(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    user = request.user
    return Response({
        'username': user.username,
        'is_admin': user.is_superuser
    })




    


