from django import forms
from .models import *


class PropertyForm(forms.ModelForm):
    
    class Meta:
        model = AllProperty
        fields = '__all__'
        exclude = ['Approval_by_Agent']


class CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = CommercialProperty
        fields = '__all__'
        exclude = ['user', 'Property_type', 'year_built','Approval_by_Agent']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Year'].widget = forms.DateInput(attrs={'type': 'date'})

class LandPropertyForm(forms.ModelForm):
    class Meta:
        model = LandProperty
        fields = '__all__'
        exclude = ['user', 'Property_type','Approval_by_Agent']

class ResidentialPropertyForm(forms.ModelForm):
    class Meta:
        model = ResidentialProperty
        fields = '__all__'
        exclude = ['user', 'Property_type', 'year_built','Approval_by_Agent']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Year'].widget = forms.DateInput(attrs={'type': 'date'})

class PropertyTypeForm(forms.Form):
    Type = forms.ChoiceField(choices=[
        ('commercial', 'Commercial'),
        ('land', 'Land'),
        ('residential', 'Residential')
    ])



class PropertyCalculatorForm(forms.Form):
    per_sqft_price = forms.FloatField(label='Per Square Feet Price', required=True)
    total_sqft = forms.FloatField(label='Total Square Feet', required=True)
    parking_sqft = forms.FloatField(label='Parking Square Feet', required=True)
    parking_price_per_sqft = forms.FloatField(label='Parking per Square Feet Price', required=True)



class PropertyFilterForm(forms.Form):
    property_type = forms.ChoiceField(choices=[('', 'All'), ('residential', 'Residential'), ('commercial', 'Commercial'), ('land', 'Land')], required=False)
    property_on = forms.ChoiceField(choices=[('', 'All'), ('rent', 'Rent'), ('sale', 'Sale')], required=False)
    area = forms.ChoiceField(choices=[('','All'), ('Gulshan','Gulshan'), ('Dhanmondi','Dhanmondi'), ('Banani', 'Banani'), ('Bashundhara R/A', 'Bashundhara R/A')], required=False)


    # Additional fields based on property type
    bedrooms = forms.IntegerField(min_value=0, required=False)
    bathrooms = forms.IntegerField(min_value=0, required=False)

    business_type = forms.ChoiceField(choices=[('', 'All'), ('office', 'Office'), ('community_center', 'Community Center'), ('shop', 'Shop'), ('other', 'Other')], required=False)
    has_conference = forms.BooleanField(required=False)
    has_security = forms.BooleanField(required=False)

    land_type = forms.ChoiceField(choices=[('', 'All'), ('Farmland', 'Farmland'), ('Playground', 'Playground'), ('warehouse', 'Warehouse')], required=False)

    ordering_choices = forms.ChoiceField(choices=[('', 'Price: Low to High'), ('price_desc', 'Price: High to Low')], required=False)



class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.EmailField()
    attachment = forms.FileField(required=False)