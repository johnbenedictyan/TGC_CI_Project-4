from django.contrib import admin
from .models import UserAccount,Group

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Group)