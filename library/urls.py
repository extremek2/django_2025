from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_library, name='index_library'),
]