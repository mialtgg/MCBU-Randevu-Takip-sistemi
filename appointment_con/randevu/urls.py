from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('calendar', calendar, name='calendar'),
    path('add_event', add_event, name='add_event'),
    path('update', update, name='update'),
    path('remove', remove, name='remove'),
    path('all_events', all_events, name='all_events'),
    path('get_events/', views.get_events, name='get_events'),
]



# urlpatterns = [
    
    
#     path("",views.randevu ,name="randevu"),
 
  
# ]
    

    
    

