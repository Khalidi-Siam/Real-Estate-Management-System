from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from RealEstate.cloudinary_utils import profile_picture_upload_to

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
    profile_picture = models.ImageField(upload_to=profile_picture_upload_to, null = True)
    is_agent = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    
@receiver(pre_delete, sender=UserProfile)
def delete_profile_pictures(sender, instance, **kwargs):
    # Cloudinary automatically handles file cleanup
    # No manual deletion needed for cloud storage
    pass


    