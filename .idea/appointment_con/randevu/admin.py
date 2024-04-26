from django.contrib import admin
from .models import Customer, Event  # Event modelini ekleyin

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'description', 'start_time', 'end_time', 'joining_date', 'status', 'admin_add_name')
    list_filter = ('status', 'joining_date')
    search_fields = ('customer_name', 'konu')

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'participations', 'start_date', 'end_date', 'user')  # Etkinlik için gerekli alanları ekleyin
    list_filter = ('start_date', 'end_date', 'user')  # Filtreleme alanlarını ekleyin
    search_fields = ('event_name', 'participations')  # Arama alanlarını ekleyin

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Event, EventAdmin)  # 

