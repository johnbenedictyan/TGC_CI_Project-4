from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm

# Create your views here.
def register(request):
    return render(request,"register.html",{
        "registerform":RegisterForm
    })
    
def login(request):
    return render(request,"login.html",{
        "loginform":LoginForm
    })
    
def logout(request):
    return redirect(login)