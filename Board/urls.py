"""
URL configuration for Board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from webpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("webpages.urls")),

    # Authentication #
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register, name='register'),
    path('boards/', views.Boards, name= 'boards'),
    path('messages/', views.Messages, name= 'messages'),
    path('board_members/', views.BoardMember, name= 'board_members'),
    path('post_message/', views.Post_Message, name='post_message'),
]
