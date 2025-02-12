from rest_framework import serializers
from .models import * 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__' #this selects all the fields that are in category models

class TagSerializer(serializers.ModelSerializer): #this serializer handles the tasks model
    class Meta:
        model = Tag 
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username') #this author is read only field and instead of displaying full name of author it only displays username

    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = Comment
        fields = "__all__"