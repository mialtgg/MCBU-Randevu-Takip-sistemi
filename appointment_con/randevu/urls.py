from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('randevu/', randevu_view, name='randevu'),
    path('rapor/', rapor_view, name='rapor'),
    path('hata', hata_view, name='hata'),
    path('succes', succes_view, name='succes'),
    path('chart/', chart_view, name='chart'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),

    

    
]





    
    

