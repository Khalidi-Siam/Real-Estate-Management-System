from django.db import models

# Create your models here.
class UserProfile(models.Model):

    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    ]
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=20, default = None)
    gender = models.IntegerField(choices=GENDER_CHOICES, default = None)
    nid = models.CharField(max_length=18, default=None)  # if Nid field is None, property dealing is cancelled.
    dob = models.DateField(default = None)

    address = models.TextField(default = None)
    profile_picture = models.ImageField(upload_to='media/profile_picture', default = None)


    