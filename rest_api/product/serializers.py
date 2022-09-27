from xml.dom import ValidationErr
from rest_framework import serializers
from product.models import  Discount,Product
class DiscountSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField()
    class Meta:
        model = Discount
        fields = ('id', 'type', 'product_discount', 'discount_amount', 'start_date', 'end_date', 'start_time', 'end_time')
    
    def validate_start_date(self, start_date):
        data = self.get_initial()
        end_date = data.get('end_date')
        
        if start_date == None and end_date != '':
            raise Exception('Start date must be present if end date is present')
        
        if start_date != '' and end_date == None:
            raise Exception('End date must be present if start date is present')

    def validate_discount_amount(self, value):
        data = self.get_initial()
        return True
        # Todo: other validation should be implemented here this way    
    
    
        

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')