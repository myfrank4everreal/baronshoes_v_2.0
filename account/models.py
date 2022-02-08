from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class SignUp(models.Model):
    email = models.EmailField()
    
    
    def __str__(self):
        return self.email
    
    
    
