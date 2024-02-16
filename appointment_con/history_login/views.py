# login_history/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LoginHistory

@login_required
def log_list(request):
    user_history = LoginHistory.objects.filter(user=request.user).order_by('-login_time')
    return render(request, 'log_list.html', {'user_history': user_history})
