from pydoc import describe
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    prod_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='greenbin/' , null = True)
    offer_status = models.BooleanField(default=False) 
    offer_price = models.IntegerField(default = 0)
    shipping_cost = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name