from django import forms
from .models import post_class
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blog_form(forms.ModelForm):
    class Meta:
        model = post_class
        fields = ['title', 'text', 'subtitle', 'img']
    
    title = forms.CharField(widget=forms.TextInput({'placeholder' : 'Enter a title'}))
    text = forms.CharField(widget=forms.Textarea({'placeholder' : 'Enter the content'}))
    subtitle = forms.CharField(widget=forms.TextInput({'placeholder' : 'Enter a subtitle'}))
    img = forms.ImageField()

class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())