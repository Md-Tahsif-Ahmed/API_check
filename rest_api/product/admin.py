from django.contrib import admin
from .models import Discount, Product

# Register your models here.
"""

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
"""
admin.site.register(Discount)
admin.site.register(Product)
 



