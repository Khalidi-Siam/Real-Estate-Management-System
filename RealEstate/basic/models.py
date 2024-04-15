from django.db import models
from authentication.models import UserProfile
from .models import *

# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 1000)
    rating = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.user.name
    
class Subscriber(models.Model):
    email = models.EmailField(unique=False)

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    