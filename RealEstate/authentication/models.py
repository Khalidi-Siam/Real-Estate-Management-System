from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, related_name = "UserProfile")
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=20, null = True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null = True)
    nid = models.CharField(max_length=18, null = True)  # if Nid field is None, property dealing is cancelled.
    dob = models.DateField(null = True)

    address = models.TextField(null = True)
    profile_picture = models.ImageField(upload_to='profile_picture', null = True)
    is_agent = models.BooleanField(default = False)

    def __str__(self):
        return self.name


    