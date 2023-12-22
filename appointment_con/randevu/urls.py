from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('randevuekle/', randevu_view, name='randevu'),
    path('rapor/', rapor_view, name='rapor'),
    path('anasayfa', succes_view, name='succes'),
    path('chart/', chart_view, name='chart'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('admindatatable/', rektördatatable_view, name='rektör_datatable'),
    path('edit_customer/<int:customer_id>/', edit_customer, name='edit_customer'),
]

    

   





    
    

