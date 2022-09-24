from django.urls import include, path 
from django.contrib import admin
#from django.conf.urls import url
 
from rest_framework import routers
from category.views import CategoryViewSet

from django.conf.urls.static import static
from django.conf import settings
 
 
router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
 
 
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)