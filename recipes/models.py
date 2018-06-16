from django.db import models

from food.models import Food, Serving, Tag


class Author(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=250, unique=True)
    colour = models.CharField(max_length=25, default='black')
    website = models.URLField(blank=True)

    class Meta:
        ordering = 'slug',

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='ingredients'
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='ingredients'
    )

    def __str__(self):
        return f'{self.food} in {self.recipe}'


class Instruction(models.Model):
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='instructions'
    )
    order = models.IntegerField(default=0)
    text = models.TextField()

    class Meta:
        ordering = 'order',

    def __str__(self):
        return f'#{self.order} of {self.recipe}'


class Recipe(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='recipes'
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='recipes'
    )
    serving = models.OneToOneField(
        Serving, on_delete=models.CASCADE, related_name='recipe'
    )
    tags = models.ManyToManyField(Tag, related_name='recipes')

    class Meta:
        ordering = 'slug',

    def __str__(self):
        return self.name
