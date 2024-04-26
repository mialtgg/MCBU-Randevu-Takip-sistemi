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
    path('delated_page/',delated_page_view,name='delated_page'),
    path('edited_page/',edited_page_view,name='edited_page'),
    path('export-to-excel/', export_to_excel, name='export_to_excel'),
    path('export-to-excel-randevu/', export_to_excel_randevu, name='export_to_excel_randevu'),
    path('phone_appointment/',phone_appointment_view,name='phone_appointment'),
    path('schedule_appointment/',schedule_appointment_view,name='schedule_appointments'),
    path('edit_events/<int:event_id>/', edit_events, name='edit_events'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
    
]

    

   





    
    

