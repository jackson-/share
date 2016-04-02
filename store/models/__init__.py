
from django.db import models
# Create your models here.


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=132)
    description = models.CharField(null=True, max_length=255)
    pricing = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    delivery_minimum = models.IntegerField(default=0)
    delivery_fee = models.IntegerField(default=0)
    est_wait_begin = models.IntegerField(default=50)
    est_wait_end = models.IntegerField(default=60)


from item import Item
from order import Order
