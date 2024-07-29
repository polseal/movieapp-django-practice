from rest_framework import serializers
from .models import Genre, Movie, Comment, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=False
    )
    class Meta:
        model = Movie
        fields = '__all__'
 
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    class Meta:
        model = Movie
        fields = fields = ['id', 'user', 'movie', 'comment']

class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movie = MovieSerializer()
    class Meta:
        model = Score
        fields = ['id', 'user', 'movie', 'rating']


