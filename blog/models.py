from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/',default='category/empty.jpg')
    title = models.CharField(max_length=255,null=True)

    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    tag = TaggableManager()
    image = models.ImageField(upload_to='blog/',default='blog/empty.jpg')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']
        
    
    def __str__(self):
        return self.title  
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
        
    
    def __str__(self):
       return self.email 
    
