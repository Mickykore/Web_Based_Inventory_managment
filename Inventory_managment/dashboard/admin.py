from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Web Based Inventory Management'

class productAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'quantity', 'price')
    list_filter = ['category']
    
admin.site.register(Product, productAdmin)
admin.site.register(Sales)
admin.site.register(Category)