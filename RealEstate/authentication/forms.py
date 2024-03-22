from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean_confirm_password(self):
        specialSym = ["$", "@", "#", "%", "*", "^", "!"]
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        if(len(password) <= 7):
            raise forms.ValidationError("Password must be at least 8 character long")
        
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must have at least one digit")
        
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password must have at least one uppercase letter")
        
        if not any(char in specialSym for char in password):
            raise forms.ValidationError("Password must have at least one special character")
        
        return confirm_password


class SignInForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Invalid email or password. Please try again."
        ),
    }
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'contact_no', 'gender', 'nid', 'dob', 'address', 'profile_picture']  # Include only necessary fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dob'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.user.pk).filter(email=email).exists():
            raise forms.ValidationError("This email already Exists")
        
        return email   


class PasswordResetConfirmForm(forms.Form):
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)
