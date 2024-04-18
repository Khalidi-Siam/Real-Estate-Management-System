from django import forms
from .models import  Bid
from django import forms
from .models import *

class Auction_PropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_Property
        fields = '__all__'
        exclude = ('seller','winner','start_time','end_time','current_price','Approval_by_Agent',)


class Auction_ResidentialPropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_ResidentialProperty
        exclude = ('Property_type','seller','winner','start_time','end_time','current_price','Approval_by_Agent',)  # Excluding Property_type because it's already defined in the parent class
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Year'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['Block'].required = False
        self.fields['Block'].label = "Block/Sector"
        
class Auction_CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_CommercialProperty
        exclude = ('Property_type','seller','winner','start_time','end_time','current_price','Approval_by_Agent',) # Excluding Property_type because it's already defined in the parent class
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Year'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['Block'].required = False
        self.fields['Block'].label = "Block/Sector"
        


class Auction_LandPropertyForm(forms.ModelForm):
    class Meta:
        model = Auc_LandProperty

        exclude = ('Property_type','seller','winner','start_time','end_time','current_price','Approval_by_Agent',)  # Excluding Property_type because it's already defined in the parent class

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Block'].required = False
        self.fields['Block'].label = "Block/Sector"


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '100', 'min': '0', 'required': True}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError("Bid amount must be a positive number.")
        return amount
    



class PropertyFilterForm(forms.Form):
    property_type = forms.ChoiceField(choices=[('', 'All'), ('residential', 'Residential'), ('commercial', 'Commercial'), ('land', 'Land')], required=False)
    area = forms.ChoiceField(choices=[('','All'), ('Gulshan','Gulshan'), ('Dhanmondi','Dhanmondi'), ('Banani', 'Banani'), ('Bashundhara R/A', 'Bashundhara R/A')], required=False)


    # Additional fields based on property type
    bedrooms = forms.IntegerField(min_value=0, required=False)
    bathrooms = forms.IntegerField(min_value=0, required=False)

    business_type = forms.ChoiceField(choices=[('', 'All'), ('office', 'Office'), ('community_center', 'Community Center'), ('shop', 'Shop'), ('other', 'Other')], required=False)
    has_conference = forms.BooleanField(required=False)
    has_security = forms.BooleanField(required=False)

    land_type = forms.ChoiceField(choices=[('', 'All'), ('Farmland', 'Farmland'), ('Playground', 'Playground'), ('warehouse', 'Warehouse')], required=False)

    ordering_choices = forms.ChoiceField(choices=[('', 'Default'), ('price_asc', 'Price: Low to High'), ('price_desc', 'Price: High to Low')], required=False)