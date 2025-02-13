from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import * 
from .serializers import *
from rest_framework import viewsets, permissions

# Create your views here.
@login_required
def like_post(request,post_id): # a function for liking the post 
    post = get_object_or_404(Post, id = post_id) # if object is there then return object otherwise give output as 404 error
    if request.user in post.likes.all():
        post.likes.remove(request.user) #if user double clicks on post the post will be unliked
    else:
        post.likes.add(request.user)
        return redirect('post',slug = post.slug) #redirects to the post detail page

@login_required
def save_post(request,post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.user in post.saved_by.all():
        post.saved_by.remove(request.user)
    else:
        post.saved_by.add(request.user)
        return redirect('post', slug = post.slug)
    

    #creating API views
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
