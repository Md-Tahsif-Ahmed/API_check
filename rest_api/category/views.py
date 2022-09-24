
''' 


# Create your views here.

class CatergoryList(APIView):
    """
    List all Categories and create new one

    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    """
    Detail, update, delete Categories  

    """
    
    def get_object(self, pk):
        try:
            categories = Category.objects.get(pk=pk)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        categories = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        categories = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categories, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categories = Category.objects.get(pk=pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
from .serializers import CategorySerializer 
from .models import Category 
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 
    def post(self, request, pk, *args, **kwargs):
        title = request.data['title']
        image = request.data['image']
      
        Category.objects.create(title=title, image=image)
        return Response(status=status.HTTP_201_CREATED)
 
    def get(self, request):
        list = Category.objects.all()
        serialize = CategorySerializer(list, many=True)
        return HttpResponse(serialize.data)

    def patch(self, request, *args, **kwargs):
        title = request.data['title']
        image = request.data['image']
      
        Category.objects.create(title=title, image=image)
        return Response(status=status.HTTP_201_CREATED)


        '''As I use ViewSet so, here i don't show PATCH,DELETE,DETAIL. Its by Default create with ViewSet'''
 
  

'''class CategorySearch(APIView):
    def get(self, request, format=None):
        data = self.request.data
        str = data['str']
         
        q = (Q(description__icontains=str)) | (Q(title__icontains=str))
        category = category.objects.filter(is_published=True)
        category = Category.objects.filter(q)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
'''



