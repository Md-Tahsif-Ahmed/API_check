from rest_framework import serializers
from product.models import  Discount,Product
class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'product_discount', 'discount_amount', 'start_date', 'end_date', 'start_time', 'end_time')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')
