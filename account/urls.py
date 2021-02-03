from django.urls import path
from django.contrib import admin

from account import views

urlpatterns = [
    path("", views.sample ,name="sample"),
    path("register" ,views.registerPage, name= "register"),
    path("login", views.loginPage, name="login"),
    path("index", views.index, name="index"),
    #path("main", views.main,name="main"),
    path("logout", views.logout_user,name="logout")


]
