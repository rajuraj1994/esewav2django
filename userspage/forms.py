from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
    def __init__(self,*args,**kwargs):
        super(ProfileUpdateForm,self).__init__(*args,**kwargs)
        self.fields.pop('password',None)
        