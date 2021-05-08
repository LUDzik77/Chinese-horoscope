from django.db import models

# Create your models here.
class Zodiac(models.Model):
    title = models.TextField()
    description = models.TextField()