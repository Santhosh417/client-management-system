from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class Vehicle(models.Model):
    year = models.CharField(max_length=4, default='2000')
    make = models.CharField(max_length=50,blank=False, null=False, default=' ')
    car_model = models.CharField(max_length=50, blank=True, null=True, default=' ')
    vin_number = models.CharField(max_length=50, default=' ')
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=5, default='2000')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.car_model

    def get_absolute_url(self):
        return reverse('vehicle_detail', args=[str(self.id)])
