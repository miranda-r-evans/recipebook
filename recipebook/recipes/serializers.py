from recipebook.recipes.models import Recipe, Comment, Rating
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.StringRelatedField(
        many=True,
        required=False
    )
    
    ingredients = serializers.StringRelatedField(
        many=True,
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'intro', 'directions', 'comments', 'ingredients', 'rating_avg']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating']