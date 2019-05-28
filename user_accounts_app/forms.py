from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ('username','first_name','last_name','email','password1','password2',)
        
    def clean_username(self):
        requested_username = self.cleaned_data.get('username')
        if UserAccount.objects.filter(username=requested_username).count() > 0:
            raise forms.ValidationError("This username is already taken!")
        return requested_username
            
    def save(self, commit=True):
        UserAccount = super(RegisterForm, self).save(commit=False)
        UserAccount.email = self.cleaned_data["email"]
        UserAccount.first_name = self.cleaned_data["first_name"]
        UserAccount.last_name = self.cleaned_data["last_name"]
 
        if commit:
            UserAccount.save()
            return UserAccount