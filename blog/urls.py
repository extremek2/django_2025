from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:pk>/', views.detail, name='blog_detail'),
    path('create/', views.create, name='blog_create'),
    path('createfake/', views.create_fake, name='blog_create_fake'),
]