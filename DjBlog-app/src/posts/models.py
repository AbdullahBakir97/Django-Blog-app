from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

'''
    title
    content
    publish_date
    
    image
    author
    tags
'''
class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=30000)
    publish_date = models.DateTimeField()
    tags = TaggableManager()