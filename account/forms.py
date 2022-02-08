from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.forms import TextInput



class CreatUser(UserCreationForm):
    class Meta:
        model = User
        
        fields=['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username':TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'name':'username',
            'placeholder':'username'
        }), 
            'email':TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'name':'email',
            'placeholder':'email'
        }),
            'password':TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'name':'password1',
            'placeholder':'password'
        }),
            'password':TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'name':'password2',
            'placeholder':'password'
        })
            
            
        }
        

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        widgets= {
            'username':TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'name':'username',
            'placeholder':'username',}), 
            
            'password':TextInput(attrs={
            'type':'password',
            'class':'form-control',
            'name':'password',
            'placeholder':'password'})
            
        }