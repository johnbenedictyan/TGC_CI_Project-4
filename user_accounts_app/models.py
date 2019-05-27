from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(blank=False,max_length=20)
    password = models.CharField(max_length=30,default="Password")
    user_email = models.EmailField(blank=False)
    user_dob = models.DateField(blank=False,auto_now=True)
    def __str__(self):
        return self.username

class Group(models.Model):
    name=models.CharField(blank=False,max_length=40)
    description = models.TextField(blank=False)
    date_created=models.DateField(blank=False,auto_now=True)
    members = models.ManyToManyField(UserAccount, related_name="groups")
    
    def __str__(self):
        return self.name    