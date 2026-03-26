from django.urls import path
from django.contrib.auth import views as auth_views # Add this
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='lawnApp/login.html'), name='login'),
]