from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/save/', views.save_post, name='save_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Your existing post detail view
    
]
