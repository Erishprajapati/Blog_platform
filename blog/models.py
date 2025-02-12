from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) #gives user friendly URL

    def __str__(self): #converts the complex data into human readable format
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True) #post are blank at first in the time of creation
    author = models.ForeignKey(User, on_delete=models.CASCADE) #user are imported
    content = models.TextField() #blank because content words can be in huge range
    created_at = models.DateTimeField(auto_now_add= True) #enables to show the created time
    updated_at = models.DateTimeField(auto_now= True) #enables to show the updated time
    published = models.BooleanField(default=False) #post are not published at first
    categories = models.ManyToManyField(Category) #post can have multiple categories
    tags = models.ManyToManyField(Tag) #post can have multiple tags 
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    saved_by = models.ManyToManyField(User, related_name='saved_posts', blank=True) #it tracks the saved post by the user
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
