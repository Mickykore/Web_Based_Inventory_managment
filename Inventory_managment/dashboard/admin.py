from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Web Based Inventory Management'

class productAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'quantity', 'price')
    list_filter = ['category']

class stafforderAdmin(admin.ModelAdmin):
    list_display= ('product_name', 'category', 'order_quantity', 'staff', 'order_date')  
class customerorderAdmin(admin.ModelAdmin):
    list_display= ('product_name', 'category', 'order_quantity', 'customer_name', 'customer_phone_no', 'staff', 'order_date') 
 
admin.site.register(Product, productAdmin)
admin.site.register(Sales)
admin.site.register(Category)
admin.site.register(OrderByCustomer, customerorderAdmin)
admin.site.register(OrderByStaff, stafforderAdmin)