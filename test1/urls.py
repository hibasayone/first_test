from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("" , views.post_blog, name = 'post_blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
