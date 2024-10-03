
from django import forms
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'first_name', 'last_name', 'gender', 'password', 'status']
