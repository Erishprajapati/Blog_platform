from django.urls import path
from .views import home, login_view, logout_view, register, profile, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    # path('profile/<int:id>/', profile, name='profile'),
    # path('post/<int:id>/', post_detail, name='post-detail'),
]
