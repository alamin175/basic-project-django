from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=30)
    recipe_description = models.TextField()
    recipe_img = models.ImageField(upload_to='recipe/')