# forms.py
from django.contrib.auth.models import User
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
class YourForm(forms.Form):
    admin_add_name = forms.ModelChoiceField(queryset=User.objects.all())