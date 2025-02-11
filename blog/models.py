from django.db import models
from django.contrib.auth.models import User

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
    

    
