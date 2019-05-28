from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

class UserAccount(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    def __str__(self):
        return self.username

class Group(models.Model):
    name=models.CharField(blank=False,max_length=40)
    description = models.TextField(blank=False)
    date_created=models.DateField(blank=False,auto_now=True)
    members = models.ManyToManyField(UserAccount, related_name="usergroups")
    
    def __str__(self):
        return self.name    