from django import forms
from .models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment', 'rating']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)