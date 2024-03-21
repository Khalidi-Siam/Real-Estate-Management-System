from django.db import models
from authentication.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
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
    Property_Pictures = models.ImageField(upload_to='pics',default=None)
    Road_No = models.CharField(max_length=4)
    Block = models.CharField(max_length=10)
    City = models.CharField(max_length=100, choices=CITY_CHOICES)
    Postal_code = models.CharField(max_length=4)
    Area = models.CharField(max_length=100, choices=AREA_CHOICES)
    Property_on = models.CharField(max_length = 20, choices=Action, null =True)
    Property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)

    def __str__(self):
        return self.Property_Name



class ResidentialProperty(AllProperty):

    House_No = models.CharField(max_length=8)
    Floor_count = models.PositiveIntegerField(default=1)
    Bedrooms = models.PositiveIntegerField(default=1)
    Bathrooms = models.PositiveIntegerField(default=1)
    Garage_spaces_Per_Sqft = models.PositiveIntegerField(default=0)
    Has_Pool = models.BooleanField(default=False)
    Has_Garden = models.BooleanField(default=False)
    Number_of_Balcony = models.PositiveIntegerField(default=1)
    Year = models.IntegerField(
        null=True,
        blank=False,
        validators=[
        MinValueValidator(1900),
        MaxValueValidator(2100)
        ]
    )

    


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
    Year = models.IntegerField(
        null=True,
        blank=False,
        validators=[
        MinValueValidator(1900),
        MaxValueValidator(2100)
        ]
    )

    

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
