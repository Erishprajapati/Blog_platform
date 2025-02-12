from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/save/', views.save_post, name='save_post'),
    # path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Your existing post detail view
]
