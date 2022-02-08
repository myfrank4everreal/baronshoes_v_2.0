from django import forms 
from .models import Comment
from django.forms import Textarea




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ['comment',]
        
        widgets={'comment':Textarea(attrs={
            'class':'form-control mb-10',
            'rows':5,
            'name':'messages',
            'placeholder':'Drop your comment'
            
        })}
        
        
        
        


