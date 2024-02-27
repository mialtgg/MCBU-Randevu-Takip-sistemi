# login_history/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LoginHistory

@login_required
def log_list(request):
    all_user_history = LoginHistory.objects.all().order_by('-login_time')
    return render(request, 'log_list.html', {'all_user_history': all_user_history})