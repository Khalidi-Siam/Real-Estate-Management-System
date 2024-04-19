from django.db import models
from authentication.models import *
from property.models import *
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    property = models.ForeignKey(AllProperty, on_delete=models.CASCADE, related_name='bookings')
    agent = models.CharField(max_length=100)
    viewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bookings_as_seller')
    time_slot = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking for {self.property.Property_Name} at {self.time_slot}"
