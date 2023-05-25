
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name= "home"),
    path ('project/<str:pk>/', views.projectpage, name = "project"),

]
