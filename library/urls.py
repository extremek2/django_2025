from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_Library, name='index_Library'),
]