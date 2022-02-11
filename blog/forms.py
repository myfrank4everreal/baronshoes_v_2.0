from django import forms 
from .models import Comment
from django.forms import TextInput, Textarea
from tinymce import TinyMCE
from .models import Post


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
        
        



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ['blog', 'headline', 'thumbnail', 'bodytext', 'content', 'category']
        
        widgets={
            'headline':TextInput(attrs={
            
            'type':'text',
            'class':'form-control',
            'name':'headline',
            'placeholder':'Headline'
        }),
            'bodytext':Textarea(attrs={
            'rows':5,
            'type':'text',
            'class':'form-control mb-5',
            'name':'headline',
            'placeholder':'Description'
        }),
            'content':TextInput(attrs={
            'rows':5,
            'type':'text',
            'class':'form-control mb-5',
            'name':'headline',
            'placeholder':'Content'
        }),
            }
  
        


