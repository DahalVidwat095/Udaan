from itertools import product

from socket import fromshare

from django import forms

from product.models import Product



class productForm(forms.ModelForm):

    class Meta:

     model = Product

     fields = ("__all__")
