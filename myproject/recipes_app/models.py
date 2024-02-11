from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipe_images/', blank=False, null=True)
    author = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'Product name: {self.name}, category: {self.categories}, author: {self.author}'
