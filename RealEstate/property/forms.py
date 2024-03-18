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

