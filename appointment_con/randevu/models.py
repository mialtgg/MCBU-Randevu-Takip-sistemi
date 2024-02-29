from django.db import models
from django.contrib.auth.models import User,Group

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.TimeField(null=True, blank=True, default=None)
    end_time = models.TimeField(null=True, blank=True, default=None)
    joining_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Active', 'Aktif'), ('Block', 'İptal Edildi')])
    admin_add_name = models.CharField(max_length=200,choices=[('mustakilban', 'M.Müştak İLBAN'),('nurdagülertürk','Nurdagül ERTÜRK'),('pelinkosan','Pelin KOŞAN'),('aysunokumus','Aysun OKUMUŞ'),('baharkocer','Bahar Koçer')])
    admin_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  
    created_time = models.TimeField(auto_now_add=True)
    deleted_time = models.DateTimeField(null=True, blank=True)
    institution_name = models.CharField(max_length=200)
    contact= models.TextField()
    status_description = models.TextField()
    type = models.CharField(max_length=20, choices=[('Face_to_face', 'Yüz Yüze'), ('Phone', 'Telefon')])
    appointment_type= models.CharField(max_length=20, choices=[('İnside', 'İç Randevu'), ('Outside', 'Dış Randevu')])
    
    

    def __str__(self):
        return self.customer_name
    

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    event_name = models.TextField()
    participations = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.event_name} "
    
class Meet (models.Model):
    name = models.TextField()
    institution_name = models.TextField()
    contact = models.DateField()
    konu = models.DateField()
    status = models.CharField(max_length=20, choices=[('Active', 'Aktif'), ('Block', 'İptal Edildi')])
    status_description = models.TextField()
    

    def __str__(self):
        return f"{self.name} "





