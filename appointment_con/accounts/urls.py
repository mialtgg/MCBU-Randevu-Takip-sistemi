from django.urls import  include, path
from .import views
from django.urls import path
from .views import logout_view



urlpatterns = [
    
    
    path("register/",views.user_register ,name="register"),
    path("",views.user_login ,name="login"),
    path("logout/",logout_view ,name="logout"),
    
    
    ]

