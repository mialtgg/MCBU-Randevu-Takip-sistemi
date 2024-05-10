# forms.py
from django.contrib.auth.models import User
from django import forms
from .models import Customer
from .models import Event

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'description', 'start_time', 'end_time','joining_date','status','institution_name','contact','status_description','type','appointment_type']
class YourForm(forms.Form):
    admin_add_name = forms.ModelChoiceField(queryset=User.objects.all())
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'participations', 'start_date', 'end_date','status_description']


