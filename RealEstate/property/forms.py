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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment', 'rating']

