from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('randevu/', randevu_view, name='randevu'),
    path('rapor/', rapor_view, name='rapor'),
    path('succes', succes_view, name='succes'),
    path('chart/', chart_view, name='chart'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('rektördatatable/', rektördatatable_view, name='rektör_datatable'),
    path('edit_customer/<int:customer_id>/', edit_customer, name='edit_customer'),
]

    

   





    
    

