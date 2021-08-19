from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("" , views.post_blog, name = 'post_blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
