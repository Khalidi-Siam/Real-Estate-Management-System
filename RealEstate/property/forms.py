from django import forms
from .models import AllProperty, CommercialProperty, LandProperty, ResidentialProperty

class PropertyForm(forms.ModelForm):
    class meta:
        model = AllProperty
        fields = "__all__"

class CommercialPropertyForm(forms.ModelForm):
    class Meta:
        model = CommercialProperty
        fields = '__all__'

class LandPropertyForm(forms.ModelForm):
    class Meta:
        model = LandProperty
        fields = '__all__'

class ResidentialPropertyForm(forms.ModelForm):
    class Meta:
        model = ResidentialProperty
        fields = '__all__'