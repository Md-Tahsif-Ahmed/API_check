from itertools import product
from django.db import models


# Create your models here.

class Discount(models.Model):
    product_discount = models.IntegerField(default=0)
    discount_amount = models.IntegerField(default=0)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField()

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

