from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)  # Add this field for the profile picture

    class Meta:
        model = CustomUser
        fields = ['username', 'profile_pic', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.profile_pic = self.cleaned_data['profile_pic']  # Save the profile picture
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser  
        fields = [
            'first_name', 'last_name', 'email', 
            'phone', 'address','postal_code','city', 'profile_pic']
