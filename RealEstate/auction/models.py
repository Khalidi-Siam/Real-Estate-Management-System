from django.db import models
from authentication.models import UserProfile
from django.db import models
from authentication.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.
class Auc_Property(models.Model):
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

    Property_Name = models.CharField(max_length=200)
    Total_area_in_sqft = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    Property_Pictures = models.ImageField(upload_to='pics',default=None)
    Road_No = models.CharField(max_length=4)
    Block = models.CharField(max_length=10)
    City = models.CharField(max_length=100, choices=CITY_CHOICES)
    Postal_code = models.CharField(max_length=4)
    Area = models.CharField(max_length=100, choices=AREA_CHOICES)
    #Property_on = models.CharField(max_length = 20, choices=Action, null =True)
    Property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    #Approval_by_Agent = models.CharField(max_length = 50, null = True)
    Property_Documents = models.FileField(upload_to='property_documents', null=True, blank=True)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='auctions')
    winner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_auctions')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If the instance is being created
            self.end_time = self.start_time + timezone.timedelta(days=2)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.Property_Name






class Auc_ResidentialProperty(Auc_Property):

    House_No = models.CharField(max_length=8)
    Floor_count = models.PositiveIntegerField(default=1)
    Bedrooms = models.PositiveIntegerField(default=1)
    Bathrooms = models.PositiveIntegerField(default=1)
    Garage_spaces_Per_Sqft = models.PositiveIntegerField(default=0)
    Has_Pool = models.BooleanField(default=False)
    Has_Garden = models.BooleanField(default=False)
    Number_of_Balcony = models.PositiveIntegerField(default=1)
    Year = models.DateField(null = True)

    


class Auc_CommercialProperty(Auc_Property):
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




class Auc_LandProperty(Auc_Property):
    Land_types = (
        ('Farmland','Farmland'),
        ('Playground','Playground'),
        ('warehouse','warehouse'),
    )
    Land_type = models.CharField(max_length=100, choices = Land_types,null = True)
    Road_size_in_sqft = models.IntegerField
    Is_fenced = models.BooleanField(default=False)


class Bid(models.Model):
    auction = models.ForeignKey(Auc_Property, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
