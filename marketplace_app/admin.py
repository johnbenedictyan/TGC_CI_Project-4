from django.contrib import admin
from .models import ListingCategory,Listing,ListingComment

# Register your models here.
admin.site.register(ListingCategory)
admin.site.register(Listing)
admin.site.register(ListingComment)