"""pub_tv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userview
from django.contrib.auth import views as autviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('screen.urls')),
    path('register/', userview.register, name='users-register'),
    path('profile/', userview.profile, name='users-profile'),
    path('login/', autviews.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout', autviews.LogoutView.as_view(template_name= 'users/logout.html'), name='logout')
]

if settings.DEBUG:#it conrols whethe you are developper server or not
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


