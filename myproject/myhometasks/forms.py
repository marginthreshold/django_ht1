from django import forms
from .models import Product


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image']

    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     widget=forms.RadioSelect)
