from django.shortcuts import redirect
from .models import LoginHistory
from django.contrib.auth import logout
from django.utils import timezone

class LoginHistoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Kullanıcı giriş yapmışsa
            if not request.session.get('login_history_tracked', False):
                # Giriş yapılan kullanıcı için bir kereye mahsus çalışacak
                login_history = LoginHistory(
                    user=request.user,
                    login_time=timezone.now(),
                    ip_address=request.META.get('REMOTE_ADDR'),
                    browser_type=request.META.get('HTTP_USER_AGENT'),
                    device_type="Mobile" if "Mobile" in request.META.get('HTTP_USER_AGENT', '') else "Desktop"
                )
                login_history.save()
                request.session['login_history_tracked'] = True
                print("123123")
            # Kullanıcı çıkış yapmışsa
                
                if request.path == 'logout/':
                    login_history = LoginHistory.objects.filter(user=request.user, logout_time__isnull=True).order_by('-login_time').first()
                    print("456")
                    if login_history:
                        login_history.logout_time = timezone.now()
                        login_history.save()
                        print("789")
                        request.session['login_history_tracked'] = False
                     

        return response
