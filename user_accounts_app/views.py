from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from project4_project import settings
# Create your views here.
def register(request):
    if request.method=="GET":
        return render(request,"register.html",{
            "registerform":RegisterForm
        })
    else:
        dirty_register_form = RegisterForm(request.POST)
        if dirty_register_form.is_valid():
            dirty_register_form.save()
            messages.success(request,"Your account has been successfully created!")
            return redirect(settings.LOGIN_URL)
        else:
            messages.error(request,"We are unable to create your account!")
            return render(request,"register.html",{
                "registerform":dirty_register_form
            })
            
    
def login(request):
    if request.method=="GET":
        return render(request,"login.html",{
            "loginform":LoginForm
        })
    else:
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        input_user = auth.authenticate(username=input_username,password=input_password)
        if input_user:
            auth.login(user=input_user,request=request)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            dirty_login_form = LoginForm(request.POST)
            messages.error(request,"Invalid login credentials")
            return render(request,"login.html",{
                "loginform":dirty_login_form
            })
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(settings.LOGOUT_REDIRECT_URL)
    
@login_required       
def account_details(request):
    return render(request,"account_details.html")