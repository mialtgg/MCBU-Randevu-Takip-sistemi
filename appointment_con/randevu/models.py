from django.db import models
from django.contrib.auth.models import User,Group

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    konu=models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    joining_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Active', 'Aktif'), ('Block', 'İptal Edildi')])
    admin_add_name = models.CharField(max_length=200,choices=[('user1', 'M.Müştak İLBAN'),('user2','Nurdagül ERTÜRK'),('user3','Pelin KOŞAN'),('user4','Aysun OKUMUŞ'),('user5','Bahar Koçer')])
    admin_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    created_time = models.TimeField(auto_now_add=True)
    deleted_time = models.DateTimeField(null=True, blank=True)
    
    
    def get_admin_name_display(self):
        return dict(self._meta.get_field('admin_add_name').flatchoices).get(self.admin_add_name, '')


    def __str__(self):
        return self.customer_name


    # randevu/models.py


class UserLoginLogoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=[('login', 'Giriş'), ('logout', 'Çıkış')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"

class UserChangeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    action = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
