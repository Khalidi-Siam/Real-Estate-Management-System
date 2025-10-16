from django.db import models
from authentication.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from RealEstate.cloudinary_utils import property_pictures_upload_to, property_documents_upload_to

# Create your models here.
class AllProperty(models.Model):
    PROPERTY_TYPES = (
        ('commercial', 'Commercial'),
        ('land', 'Land'),
        ('residential', 'Residential'),
    )
    Action = (
        ('rent','Rent'),
        ('sale','Sale'),
    )

    CITY_CHOICES = (
        ('Dhaka', 'Dhaka'),
    )
    AREA_CHOICES = (
        ('Gulshan', 'Gulshan'),
        ('Banani', 'Banani'),
        ('Dhanmondi', 'Dhanmondi'),
        ('Bashundhara R/A', 'Bashundhara R/A'),
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='properties', null = True)
    Property_Name = models.CharField(max_length=200)
    Property_Description = models.TextField(null=True, blank=True)
    Total_area_in_sqft = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    Price = models.IntegerField(default=0)
    Property_Pictures = models.ImageField(upload_to=property_pictures_upload_to)
    Road_No = models.CharField(max_length=4)
    Block = models.CharField(max_length=10)
    City = models.CharField(max_length=100, choices=CITY_CHOICES)
    Postal_code = models.CharField(max_length=4)
    Area = models.CharField(max_length=100, choices=AREA_CHOICES)
    Property_on = models.CharField(max_length = 20, choices=Action, null =True)
    Property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    Approval_by_Agent = models.CharField(max_length = 50, null = True)
    Property_Documents = models.FileField(upload_to=property_documents_upload_to)
    needs_approval = models.BooleanField(default= False)

    def __str__(self):
        return self.Property_Name



@receiver(pre_delete, sender=AllProperty)
def delete_property_pictures(sender, instance, **kwargs):
    # Cloudinary automatically handles file cleanup
    # No manual deletion needed for cloud storage
    pass

@receiver(pre_delete, sender=AllProperty)
def delete_property_documents(sender, instance, **kwargs):
    # Cloudinary automatically handles file cleanup
    # No manual deletion needed for cloud storage
    pass


class ResidentialProperty(AllProperty):

    House_No = models.CharField(max_length=8)
    Floor_count = models.PositiveIntegerField(default=1)
    Bedrooms = models.PositiveIntegerField(default=1)
    Bathrooms = models.PositiveIntegerField(default=1)
    Garage_spaces_Per_Sqft = models.PositiveIntegerField(default=0)
    Has_Pool = models.BooleanField(default=False)
    Has_Garden = models.BooleanField(default=False)
    Number_of_Balcony = models.PositiveIntegerField(default=1)
    Year = models.DateField(null = True)

    


class CommercialProperty(AllProperty):
    Business_types = (
        ('office', 'Office'),
        ('community_Center', 'community_Center'),
        ('shop', 'Shop'),
        ('other', 'Other')
        
    )
    House_No = models.CharField(max_length=8)
    Business_type = models.CharField(max_length=20, choices=Business_types,null =True)
    Parking_spaces = models.PositiveIntegerField(default=0)
    Has_elevator = models.BooleanField(default=False)
    Has_security_system = models.BooleanField(default=False)
    Has_conference_room = models.BooleanField(default=False)
    Year = models.DateField(null = True)

    

class LandProperty(AllProperty):
    Land_types = (
        ('Farmland','Farmland'),
        ('Playground','Playground'),
        ('warehouse','warehouse'),
    )
    Land_type = models.CharField(max_length=100, choices = Land_types,null = True)
    Road_size_in_sqft = models.IntegerField
    Is_fenced = models.BooleanField(default=False)


class SavedSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    criteria = models.JSONField()  # Store filter criteria as JSON data

    def __str__(self):
        return self.name
