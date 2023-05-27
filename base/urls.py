
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name= "home"),
    path ('project/<str:pk>/', views.projectpage, name = "project"),
    path('add-project/', views.addproject, name="add-project"),
    path('edit-project/<str:pk>/', views.editproject, name="edit-project"),
    path('inbox/', views.inboxPage, name="inbox"),
    
]
