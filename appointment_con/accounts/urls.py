from django.urls import  include, path
from .import views


urlpatterns = [
    
    
    path("register/",views.user_register ,name="register"),
    path("",views.user_login ,name="login"),
    path("logout/",views.user_logout ,name="logout"),
    path('delete/<int:data_id>/', views.delete_data_view, name='delete_data_view'),
    
    ]

