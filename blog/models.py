from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    #category
    #tags
    img = models.ImageField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title  