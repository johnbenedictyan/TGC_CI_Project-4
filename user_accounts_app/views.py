from django.shortcuts import render

# Create your views here.
def register(request):
    return(render,"register.html")
    
def login(request):
    return(render,"login.html")
    
