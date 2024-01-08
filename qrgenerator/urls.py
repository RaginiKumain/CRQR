

from django.urls import path
from .views import qrgenerator

app_name = 'qrgenerator'

urlpatterns = [
    path('', qrgenerator, name='qrgenerator'),
    
    # Add more URL patterns as needed
]






