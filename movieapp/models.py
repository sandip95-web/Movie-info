from django.db import models

# Create your models here.
class Rate(models.Model):
    username=models.CharField(max_length=50,null=False,blank=False,default="")
    rate_id=models.CharField(max_length=100,null=False,blank=False)
    vote=models.CharField(max_length=100,null=True,blank=False)
    created_at=models.DateTimeField(auto_now=True)
    
    
class Comment(models.Model):
    username=models.CharField(max_length=50,null=False,blank=False,default="")
    comment_id=models.CharField(max_length=100,null=False,blank=False)
    comment=models.TextField(max_length=500,null=True,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
class Favourite(models.Model):
    username=models.CharField(max_length=50,null=True,blank=False,default="")
    movie_id=models.CharField(max_length=100,null=True,blank=False)
    movie_title=models.TextField(max_length=500,null=True,blank=False)
    movie_image=models.TextField(max_length=500,null=True,blank=True)
    