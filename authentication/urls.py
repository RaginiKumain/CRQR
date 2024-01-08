

from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, home, dashboard

app_name = 'authentication'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    # Add more URL patterns as needed
]






