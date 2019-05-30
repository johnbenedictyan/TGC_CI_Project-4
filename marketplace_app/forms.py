from django import forms
from .models import Listing,ListingImage

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name','description','price','location','categories','used')

class ListingImageForm(forms.ModelForm):
    image = forms.ImageField(label='Listing Image')  
    class Meta:
        model = ListingImage
        fields = ('image',)