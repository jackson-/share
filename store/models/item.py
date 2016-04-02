from django.db import models
from store.models import Store

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, default=None)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=132, null=True)
    eighth_price = models.FloatField()
    quarter_price = models.FloatField()
    half_price = models.FloatField()
    ounce_price = models.FloatField()
    link = models.URLField(max_length=255, null=True)