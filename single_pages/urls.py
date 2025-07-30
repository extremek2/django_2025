# from sesac_django_project.urls import urlpatterns
# sesac_django_project/urls.py

from django.urls import path

# single_pages/views.py
from . import views
from .views import landing

urlpatterns = [
    path('', views.landing, name='landing'),
]