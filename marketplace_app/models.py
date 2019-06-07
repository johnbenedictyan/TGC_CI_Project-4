from django.db import models
from user_accounts_app.models import UserAccount
from pyuploadcare.dj.models import ImageField
from project4_project import settings

# Create your models here.
class ListingCategory(models.Model):
    name = models.CharField(blank=False,max_length = 255)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.name
    
class Listing(models.Model):
    name = models.CharField(blank=False,max_length = 255)
    description = models.TextField(blank=False)
    price = models.FloatField(blank=False,default=0.0)
    location = models.CharField(blank=False,max_length = 255)
    categories = models.ManyToManyField(ListingCategory, related_name="listings")
    used = models.BooleanField(blank=False,default=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="listings")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_listings")
    listing_photo = ImageField(blank=False)
    date_time_listed = models.DateTimeField(auto_now_add=True, blank=True)
    potential_buyers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="potential_purchases")
    sold = models.BooleanField(blank=True,default=False)
    
    def __str__(self):
        return self.name    
        
class ListingComment(models.Model):
    comment = models.TextField(blank=False)
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name="comments")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="comments")
    

class Order(models.Model):
    ordered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='orders')
    stripe_token = models.CharField(max_length=1000, blank=False)
    date_of_purchase = models.DateTimeField(blank=False)
    
    def __str__(self):
        return "Order - " + str(self.id)
    