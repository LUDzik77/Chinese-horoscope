from django.db import models
from django.urls import reverse

# Create your models here.
class Postentry(models.Model):
    author = models.CharField(max_length=180)
    description = models.TextField()
    
    def get_absolute_url(self):
        #return(reverse("guestbook:Postentry-list", kwargs={"id":self.id}))    #Postentry-detail  Postentry_list?
        return(reverse("guestbook:Postentry-list"))
    