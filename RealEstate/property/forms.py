from django import forms
from .models import *

class PropertyForm(forms.ModelForm):
    class Meta:
        model = AllProperty
        fields = '__all__'
        


class CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = CommercialProperty
        fields = '__all__'
        exclude = ['user', 'Property_type', 'year_built']

class LandPropertyForm(forms.ModelForm):
    class Meta:
        model = LandProperty
        fields = '__all__'
        exclude = ['user', 'Property_type']

class ResidentialPropertyForm(forms.ModelForm):
    class Meta:
        model = ResidentialProperty
        fields = '__all__'
        exclude = ['user', 'Property_type', 'year_built']

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


