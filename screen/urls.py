from django.urls import path
from . import views
from django.contrib.auth import views as autviews
from django.contrib.auth.models import User



if User.is_authenticated:
    urlpatterns = [
        path('home/', views.home, name='screen-home'),
        path('about/', views.about, name='screen-about'),
        path('', views.home, name='screen-home'),
        path('videolist/', views.videolist, name='screen-videolist')
    ]

else:
    urlpatterns = [
        path('home/', views.home, name='screen-home'),
        path('about/', views.about, name='secreen-about'),
        path('', autviews.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    ]
