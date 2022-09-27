from itertools import product
from pydoc import describe
from .serializers import DiscountSerializer, ProductSerializer
from .models import Discount, Product
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.db.models import Q
 

class DiscountList(APIView):
    """
    List all All Discount and create new one

    """

    def get(self, request, format=None):
        discount = Discount.objects.all()
        serializer = DiscountSerializer(discount, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiscountSerializer(data=request.data)
        
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'msg': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
            
class DiscountDetail(APIView):
    """
    Detail, update, delete Discount  

    """
    
   
    
    def get_object(self, pk):
        try:
            discount =  Discount.objects.get(pk=pk)

        except Discount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        discount = Discount.objects.get(pk=pk)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        discount = Discount.objects.get(pk=pk)
        serializer = DiscountSerializer(discount, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        discount = Discount.objects.get(pk=pk)
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiscountSearch(APIView):
    def get(self, request, format=None):
        data = self.request.query_params
        str = 'per'
         
        q = (Q(type__icontains=str))
        # discount = Discount.objects.filter(is_published=True)
        discount = Discount.objects.filter(q)
        serializer = DiscountSerializer(discount, many=True)
        return Response(serializer.data)




class ProductList(APIView):
    """
    List all Categories and create new one

    """

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(Http404)


class ProductDetail(APIView):
    """
    Detail, update, delete Categories  

    """
    
    def get_object(self, pk):
        try:
            product = Product.objects.get(pk=pk)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductSearch(APIView):
    def get(self, request, format=None):
        data = self.request.data
        str = data['str']
        #price=data['price']
        q = (Q(description__icontains=str)) | (Q(title__icontains=str))
        product = Product.objects.filter(is_published=True)
        product = product.objects.filter(q)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


