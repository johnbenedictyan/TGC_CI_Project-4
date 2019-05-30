from django.db import models
from user_accounts_app.models import UserAccount

# Create your models here.
class ListingCategory(models.Model):
    name = models.CharField(blank=False,max_length = 255)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.name
        
class ListingImage(models.Model):
    image = models.ImageField(upload_to='images')
    
class Listing(models.Model):
    name = models.CharField(blank=False,max_length = 255)
    description = models.TextField(blank=False)
    price = models.FloatField(blank=False,default=0.0)
    location = models.CharField(blank=False,max_length = 255)
    categories = models.ManyToManyField(ListingCategory, related_name="listings")
    used = models.BooleanField(blank=False,default=False)
    seller = models.ForeignKey(UserAccount,on_delete=models.CASCADE, related_name="listings")
    likes = models.ManyToManyField(UserAccount, related_name="liked_listings")
    images = models.ManyToManyField(ListingImage,related_name="listings")
    def __str__(self):
        return self.name    
        
class ListingComment(models.Model):
    comment = models.TextField(blank=False)
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name="comments")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="comments")
    

    