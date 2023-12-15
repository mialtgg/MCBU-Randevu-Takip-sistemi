from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('randevu/', randevu_view, name='randevu'),
    path('save_event/', save_event, name='save_event'),
    path('rapor/', rapor_view, name='rapor')
]





    
    

