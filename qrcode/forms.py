from socket import fromshare
from django import forms


from accounts.models import User
from .models import QRCode


class QRCodeForm(forms.ModelForm):
    url_or_message = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter URL or Message', 
        'id': '',
        }))
    name = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter a name of this QRCode', 
        'id': '',
        }))


    class Meta:
        model = QRCode
        fields = ['url_or_message', 'name']
