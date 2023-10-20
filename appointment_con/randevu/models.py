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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    

