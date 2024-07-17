from django.db import models
from django.db.models import Avg

class Recipe(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    title = models.CharField(max_length=200)
    intro = models.TextField()
    directions = models.TextField()

    # In a production-ready implementation, a script would recalculate the rating at a set interval,
    # rather than everytime this value is queried.
    @property
    def rating_avg(self):
        return self.rating_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.title

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.content

class Ingredient(models.Model):
    name = models.CharField(max_length=50, blank=False)
    recipes = models.ManyToManyField(Recipe, through='RecipeIngredient')

    def __str__(self):
        return str(self.name)

# Splitting ingredient into its own table will be useful for feature development, i.e. searching by ingredient.
# Splitting quantity is not as useful, but would probably be a good database optimization.
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return str(self.quantity + ' ' + self.ingredient.name)

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.rating)