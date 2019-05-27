from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirmpassword = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    class Meta:
        model = UserAccount
        fields = ('username', 'email', 'password', 'confirmpassword')
        
    def clean_email(self):
        requested_username = self.cleaned_data.get('username')
        if UserAccount.objects.filter(username=requested_username).count() > 0:
            raise forms.ValidationError("This username is already taken!")
        return requested_username
            
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')
        if (password != confirmpassword):
            raise forms.ValidationError("The password do not match")
        return confirmpassword