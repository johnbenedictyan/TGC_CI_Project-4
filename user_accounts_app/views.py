from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from project4_project import settings
from .models import UserAccount,Group
# Create your views here.
def register(request):
    if request.method=="GET":
        register_form = RegisterForm()
        return render(request,"register.html",{
            "register_form":register_form
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
                "register_form":dirty_register_form
            })
            
    
def login(request):
    if request.method=="GET":
        login_form=LoginForm()
        return render(request,"login.html",{
            "login_form":login_form
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
                "login_form":dirty_login_form
            })

@login_required    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(settings.LOGOUT_REDIRECT_URL)
    
@login_required       
def account_details(request):
    current_user_id = request.session.get('_auth_user_id')
    current_user_id = request.user.id
    current_user_details = UserAccount.objects.all().get(pk=current_user_id)
    return render(request,"account_details.html",{
        "current_user_details":current_user_details
    })
    