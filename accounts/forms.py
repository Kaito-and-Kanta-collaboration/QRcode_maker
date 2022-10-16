from django import forms 
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='確認パスワード', widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ('username', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'is_staff', 'is_active', 'is_superuser' )

    def clean_password(self):
        return self.initial['password']