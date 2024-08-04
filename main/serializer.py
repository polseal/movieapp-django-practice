from rest_framework import serializers
from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=False
    )
    class Meta:
        model = Movie
        fields =  ['id', 'title', 'year', 'genre', 'summary']
 



