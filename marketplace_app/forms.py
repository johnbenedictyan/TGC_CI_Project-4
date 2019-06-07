from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Listing
from pyuploadcare.dj.forms import FileWidget, ImageField

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
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('price', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'description',
            'location',
            Row(
                Column('categories', css_class='form-group col-md-6 mb-0 categories_form_custom_css'),
                Column('listing_photo', css_class='form-group col-md-4 mb-0'),
                Column('used', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Create Listing', css_class="btn essence-btn")
        )
        
class PaymentForm(forms.Form):
    # cc, cvc, expiry date
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2039)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('credit_card_number', css_class='form-group col mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('expiry_month', css_class='form-group col-md-3 mb-0 categories_form_custom_css'),
                Column('expiry_year', css_class='form-group col-md-3 mb-0'),
                Column('cvv', css_class='form-group col-md-6 mb-0'),
                css_class='form-row my-2'
            ),
            Row(
                Column('stripe_id', css_class='form-group col mb-0'),
                css_class='form-row my-2'
            ),
            Row(
                Submit('submit', 'Pay', css_class="btn essence-btn mx-auto"),
                css_class='my-2'
            ),
            
        )