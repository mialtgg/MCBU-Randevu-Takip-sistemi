from django.contrib import admin

from randevu.models import *

from .models import UserActivity

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'activity_type')





