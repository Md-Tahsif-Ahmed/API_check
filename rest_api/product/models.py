from itertools import product
from random import choices
from secrets import choice
from django.db import models

from product.enum import DiscountType


# Create your models here.

class Discount(models.Model):
    product_discount = models.IntegerField(default=0)
    discount_amount = models.IntegerField(default=0)
    type = models.CharField(default=DiscountType.FLAT_AMOUNT, choices=DiscountType.CHOICES, max_length=12)
    start_date = models.DateField(null = True) 
    end_date = models.DateField(null = True)
    start_time = models.TimeField(null = True)
    end_time = models.TimeField(null = True)

    flat_amount = models.IntegerField(default=0)
    percentage_amount = models.IntegerField(default=0)

    class Meta:
        def __str__(self):
            return self.discount_amount


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    '''discount = models.ForeignKey(Discount, on_delete=models.CASCADE)'''
    

    class Meta:
        def __str__(self):
            return self.title

