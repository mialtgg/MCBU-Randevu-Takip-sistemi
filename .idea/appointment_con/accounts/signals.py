

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone
from .models import UserLog

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    UserLog.objects.create(user=user, login_time=timezone.now())

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    user_log = UserLog.objects.get(user=user, logout_time__isnull=True)
    user_log.logout_time = timezone.now()
    user_log.save()
