# cart/forms.py

from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
