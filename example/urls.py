from django.urls import path
from . import views

urlpatterns = [
    path('', views.example, name='example_index'),
    path('map/', views.examplemap, name='example_map'),
    path('helloAPI', views.helloAPI, name='helloAPI'),
    path('hiAPI', views.hiAPI, name='hiAPI'),
    path('postAPI/<int:pk>/', views.postAPI, name='postAPI'),
    path('blogAPI/', views.blogAPI, name='blogAPI'),
]
