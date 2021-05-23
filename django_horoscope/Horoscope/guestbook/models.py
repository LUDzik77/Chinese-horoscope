from django.db import models
from django.urls import reverse

# Create your models here.
class Postentry(models.Model):
    author = models.TextField()
    description = models.TextField()
    
    def get_absolute_url(self):
        return(reverse("guestbook:Postentry-list", kwargs={"id":self.id}))    #Postentry-detail  Postentry_list?
    