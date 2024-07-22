"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import *

from . import views


# Url patterns for Books app module of Library Management System
urlpatterns = [
    path("", views.home, name="home"),
    path("issue", views.issue, name="issue"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("return_item", views.return_item, name="return_item"),
    path("history", views.history, name="history"),
    path("login/register", views.register, name="register"),
]