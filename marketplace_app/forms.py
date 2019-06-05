from django import forms
from .models import Listing
from pyuploadcare.dj.forms import FileWidget, ImageField,ImageGroupField

class ListingForm(forms.ModelForm):
    listing_photo = ImageField(widget=FileWidget(attrs={
        'data-public-key':'c1c0ea35a4b3421770fa',
        'data-images-only':'True',
        'data-preview-step':'True',
    }))
    class Meta:
        model = Listing
        fields = ('name','description','price','used','location','listing_photo','categories')
        exclude = ['seller']