from django import forms
from .models import  Bid
from django import forms
from .models import *

class Auction_PropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_Property
        fields = '__all__'
        exclude = ('seller','winner','end_time','current_price')

class Auction_ResidentialPropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_ResidentialProperty
        exclude = ('Property_type','seller','winner','end_time','current_price')  # Excluding Property_type because it's already defined in the parent class

class Auction_CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_CommercialProperty
        exclude = ('Property_type','seller','winner','end_time','current_price') # Excluding Property_type because it's already defined in the parent class

class Auction_LandPropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_LandProperty
        exclude = ('Property_type','seller','winner','end_time','current_price')  # Excluding Property_type because it's already defined in the parent class


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
