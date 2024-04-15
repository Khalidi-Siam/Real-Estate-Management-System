from django.db import models
from authentication.models import *
from auction.models import *


# Create your models here.

class PaymentDetails(models.Model):
    name = models.CharField(max_length=233)
    property_name = models.CharField(max_length=233)
    payment_time = models.DateTimeField(auto_now_add = True)
    payment_amount = models.IntegerField()
    property_id  =  models.ForeignKey(Auc_Property, on_delete=models.CASCADE, null = True)
    owner_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null = True)
    
    
    