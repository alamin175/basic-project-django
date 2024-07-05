from django.db import models

# Create your models here.
class Learning(models.Model):
    learnId = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)