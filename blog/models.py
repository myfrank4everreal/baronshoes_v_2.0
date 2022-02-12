from django.db import models
from django.contrib.auth.models import User 
from tinymce import HTMLField




class Blog(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.TextField()
    blog_image = models.ImageField()
    
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, null = True)
    
    def __str__(self):
        return self.user.username
    
    
class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=300)
    thumbnail = models.ImageField(blank=True, null=True)
    bodytext = models.TextField()
    content = HTMLField('content')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False, blank=True, null=True)
    # viewcount = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    prevpost = models.ForeignKey('self', related_name='previous_post', on_delete=models.SET_NULL, blank=True, null=True )
    nextpost = models.ForeignKey('self', related_name='next_post', on_delete=models.SET_NULL, blank=True, null=True )
    
    
    def __str__(self):
        return self.headline
    
    def shotend_bodytext(self):
        return self.bodytext[:200] + '...'
    
    @property
    def get_comment_count(self):
        return self.comment_set.count()
    
    
    @property
    def get_thumbnail(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        else:
            return "static/mysite/img/blog/add.jpg"
    
    
    def get_next_post(self):
        return self.nextpost
    
    def get_next_post(self):
        return self.prevpost
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    