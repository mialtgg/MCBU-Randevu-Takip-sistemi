from . import views
from django.urls import path
from .views import *

urlpatterns=[
    path('log-list/', log_list, name='log_list'),
    
]