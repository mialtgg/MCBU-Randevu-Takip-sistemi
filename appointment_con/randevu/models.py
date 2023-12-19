from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    konu=models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    joining_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Block', 'Block')])

    def __str__(self):
        return self.customer_name


