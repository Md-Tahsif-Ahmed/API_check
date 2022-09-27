from django.urls import path 
from . import views

  
 
 
urlpatterns = [
    
     path('products/', views.ProductList.as_view(), name='list'),
     path('products/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
     path('products_search/', views.ProductSearch.as_view(), name='search'),
     path('discounts', views.DiscountList.as_view(), name='list'),
     path('discounts/<int:pk>/', views.DiscountDetail.as_view(), name='list'),
     path('discounts_search/', views.DiscountSearch.as_view(), name='search'),
 
]

