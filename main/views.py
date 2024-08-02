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

@api_view(['GET'])
def get_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_movie(request):
    data=request.data
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        publish_message({'movie': data.id, 'title': data.title, 'status': 'created'})
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    movie.delete()
    publish_message(
        message_body={
            'action': 'deleted',
            'title': serializer.data['title'],
            'description': serializer.data['description']
        }
    )

    return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
   



    


