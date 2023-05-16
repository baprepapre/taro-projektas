from typing import Any, Dict
from .models import Profile
from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=150,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, 
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise forms.ValidationError('Šis el. pašto adresas jau yra naudojamas')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exclude(username=self.instance.username).exists():
            raise forms.ValidationError('Šis vartotojo vardas jau yra naudojamas')
        return username



