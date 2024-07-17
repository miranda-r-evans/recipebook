from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recipebook.recipes.models import Recipe
from .serializers import RecipeSerializer, CommentSerializer, RatingSerializer

# This could be improved by an option to provide only specified fields, since we only need id, name, and rating for this API call in our current implementation
class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecipeDetailView(APIView):
    def get(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Recipe.DoesNotExist:
            return Response(
                {"res": "Object with recipe id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

class CommentDetailView(APIView):
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            recipeSerializer = RecipeSerializer(recipe)
            data = request.data
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save(recipe_id=recipe_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Recipe.DoesNotExist:
            return Response(
                {"res": "Object with recipe id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

class RatingDetailView(APIView):
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            recipeSerializer = RecipeSerializer(recipe)
            data = request.data
            serializer = RatingSerializer(data=data)
            if serializer.is_valid():
                serializer.save(recipe_id=recipe_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print('not valid')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Recipe.DoesNotExist:
            return Response(
                {"res": "Object with recipe id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )