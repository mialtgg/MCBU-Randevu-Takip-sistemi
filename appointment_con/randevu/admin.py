from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'description', 'start_time', 'end_time', 'joining_date', 'status','admin_add_name')
    list_filter = ('status', 'joining_date')
    search_fields = ('customer_name', 'konu')

admin.site.register(Customer, CustomerAdmin)
