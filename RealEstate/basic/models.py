from django.db import models
from authentication.models import UserProfile

# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    comment = models.TextField(max_length = 1000)
    rating = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.user.name
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    