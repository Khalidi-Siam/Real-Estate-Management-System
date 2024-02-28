from django import forms
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'name', 'email'
        ]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'