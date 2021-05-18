from django.db import models

# Create your models here.
class Postentry(models.Model):
    author = models.TextField()
    description = models.TextField()