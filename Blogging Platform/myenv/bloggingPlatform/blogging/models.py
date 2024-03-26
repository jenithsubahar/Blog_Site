from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)


class Log(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.post.title} at {self.created_at}'
