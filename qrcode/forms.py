from django import forms


from accounts.models import User
from .models import QRCode


class CreateQRCodeForm(forms.ModelForm):
    url_or_message = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg', 
        'placeholder': 'Enter URL or Message', 
        'type': 'text',
        'aria-label': '.form-control-lg',
        }))
        
    name = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter URL or Message', 
        'type': 'text',
        'aria-label': 'default input',
        }))


    class Meta:
        model = QRCode
        fields = ['url_or_message', 'name']
