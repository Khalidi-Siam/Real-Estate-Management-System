from django.db import models
from authentication.models import UserProfile

# Create your models here.
class AllProperty(models.Model):
    PROPERTY_TYPES = (
        ('commercial', 'Commercial'),
        ('land', 'Land'),
        ('residential', 'Residential'),
    )
    Action = (
        ('rent','Rent'),
        ('sell','Sell'),
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='properties', null = True)
    Property_Name = models.CharField(max_length=200)
    Property_Description = models.TextField(null=True, blank=True)
    Price = models.IntegerField(default=0)
    Property_Pictures = models.ImageField(upload_to='pics',default=None)
    Road_No = models.CharField(max_length=4)
    Block = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=4)
    District = models.CharField(max_length=100)
    Property_on = models.CharField(max_length = 20, choices=Action, null =True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)



class ResidentialProperty(AllProperty):

    House_No = models.CharField(max_length=8)
    floor_count = models.PositiveIntegerField(default=1)
    bedroom_count = models.PositiveIntegerField(default=1)
    bathroom_count = models.PositiveIntegerField(default=1)
    garage_spaces = models.PositiveIntegerField(default=0)
    has_pool = models.BooleanField(default=False)
    has_garden = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)
    year_built = models.DateField(null=True, blank=True)

    



class CommercialProperty(AllProperty):

    House_No = models.CharField(max_length=8)
    business_type = models.CharField(max_length=100)
    total_area = models.DecimalField(max_digits=8, decimal_places=2)
    parking_spaces = models.PositiveIntegerField(default=0)
    has_elevator = models.BooleanField(default=False)
    has_security_system = models.BooleanField(default=False)
    has_conference_room = models.BooleanField(default=False)
    year_built = models.DateField(null=True, blank=True)

    

class LandProperty(AllProperty):
    land_area = models.DecimalField(max_digits=8, decimal_places=2)
    land_type = models.CharField(max_length=100)
    road_access = models.BooleanField(default=True)
    is_fenced = models.BooleanField(default=False)

    
