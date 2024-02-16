# your_app_name/signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # Kullanıcının tarayıcı bilgisini al
    user_agent = request.META.get('HTTP_USER_AGENT', 'Bilinmeyen Cihaz')

    # Mobil cihazı belirleme
    is_mobile = 'Mobil' in user_agent

    # Mobil cihaz bilgisini print et
    print(f"Kullanıcı {user.username}'nin cihazı mobil mi: {is_mobile}")
