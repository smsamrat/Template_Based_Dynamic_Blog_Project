from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blog')
    blog_title = models.CharField(max_length=200,blank=False, null=False)
    slug = models.SlugField(max_length=200,unique=True)
    blog_content = models.TextField(blank=False, null=False)
    blog_image = models.ImageField(upload_to="blog_image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title

class Commnet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment_text

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like')
    def __str__(self):
        return self.user+"Likes"+self.blog
    class Meta:
        verbose_name = 'Likes'
        verbose_name_plural = 'Likes'
    
