from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post #import post because we only work in post now

# Create your views here.
@login_required
def like_post(request,post_id): # a function for liking the post 
    post = get_object_or_404(Post, id = post_id) # if object is there then return object otherwise give output as 404 error
    if request.user in post.likes.all():
        post.likes.remove(request.user) #if user double clicks on post the post will be unliked
    else:
        post.likes.add(request.user)
        return redirect('post-detail',slug = post.slug) #redirects to the post detail page

@login_required
def save_post(request,post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.user in post.saved_by.all():
        post.saved_by.remove(request.user)
    else:
        post.saved_by.add(request.user)
        return redirect('post_detail', slug = post.slug)