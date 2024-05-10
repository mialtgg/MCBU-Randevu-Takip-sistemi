from django.urls import   path
from .import views
from django.urls import path
from .views import *



urlpatterns = [
    
    
    path("register/",views.user_register ,name="register"),
    path("",views.user_login ,name="login"),
    path("logout/",logout_view ,name="logout"),
    path('password_change/', password_change, name='password_change'),
    
    
    ]

