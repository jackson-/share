from django.db import models
from store.models.item import Item
from registration.models.user import MyUser

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customers = models.ManyToManyField(MyUser)
    item = models.ForeignKey(Item)
    status = models.CharField(max_length=64)
    description = models.CharField(max_length=132, null=True)
    current_total = models.FloatField()
    price = models.FloatField()


