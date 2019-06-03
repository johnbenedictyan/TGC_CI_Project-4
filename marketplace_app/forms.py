from django import forms
from .models import Listing
from pyuploadcare.dj.forms import FileWidget, ImageField,ImageGroupField

class ListingForm(forms.ModelForm):
    listing_images = ImageGroupField(widget=FileWidget(attrs={
        'data-public-key':'c1c0ea35a4b3421770fa',
        'data-multiple':'True',
        'data-multiple-max':'4',
        'data-images-only':'True',
        'data-preview-step':'True',
        'data-crop':'crop',
        'data-image-shrink':'500x500'
    }))
    class Meta:
        model = Listing
        fields = ('name','description','price','used','location','listing_images','categories')
