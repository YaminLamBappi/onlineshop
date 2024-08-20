# forms.py
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'postal_code', 'city', 'payment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            profile = getattr(user, 'userprofile', None)
            if profile:
                self.fields['first_name'].initial = user.first_name
                self.fields['last_name'].initial = user.last_name
                self.fields['phone'].initial = profile.phone
                self.fields['address'].initial = profile.address
                self.fields['postal_code'].initial = profile.postal_code
                self.fields['city'].initial = profile.city
