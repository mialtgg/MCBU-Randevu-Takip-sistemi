from django import forms
from django.db import models

from django.db import models
from pkg_resources import require

# class Randevu(models.Model):
#     ad_soyad = models.CharField(max_length=100)
#     tarih = models.DateTimeField()
#     randevu_konusu = models.TextField()
#     iletisim =models.TextField()
#     sonuc_ekranı=models.TextField()
#     saatS = models.TimeField()
#     saatF = models.TimeField()
#     oncelik = models.IntegerField(choices=[(1, '1. Derece öncelikli '), (2, '2. Derece öncelikli')])
    
#     class meta:
#         ['ad_soyad','tarih','randevu_konusu','iletisim','sonuc_ekranı','saatS','saatF','oncelik']

class Events(models.Model):
        PRIORITY_CHOICES = [
        ('Low', 'Düşük'),
        ('Medium', 'Orta'),
        ('High', 'Yüksek'),
    ]
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=255, verbose_name='Event Name', null=True)
        description = models.TextField(verbose_name='Description', null=True)
        priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, verbose_name='Priority', default='Low', null=True)
        date = models.DateField(verbose_name='Event Date', default='2023-01-01', null=True)
        all_day = models.BooleanField(verbose_name='All Day Event', default=True, null=True)
        start_time = models.TimeField(blank=True, null=True, verbose_name='Start Time', default='08:00:00')
        end_time = models.TimeField(blank=True, null=True, verbose_name='End Time', default='17:00:00')
        location = models.CharField(max_length=255, verbose_name='Location', null=True, default='***********')
        


        def __str__(self):
         return self.name
        
        

