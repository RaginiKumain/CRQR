from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomUserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_('Confirm Password'))

    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Add other fields as needed

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Passwords do not match.'))
        return password2

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser  # Use your CustomUser model
