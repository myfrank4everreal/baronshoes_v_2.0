from django.db import models
from django.contrib.auth.models import User 




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
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False, blank=True, null=True)
    viewcount = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
    
    # def get_comment(self):
    #     return self.comment_set.all()
    
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    