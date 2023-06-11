from django import forms
from .models import Product, Category, Sales, OrderByCustomer, OrderByStaff
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        
class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product_name', 'sale_price', 'sale_quantity', 'staff']
        

class CustomerOrderForm(forms.ModelForm):

    class Meta:
        model = OrderByCustomer
        fields = ['product_name', 'category', 'order_quantity', 'customer_name', 'customer_phone_no', 'staff', 'order_date']

class StaffOrderForm(forms.ModelForm):

    class Meta:
        model = OrderByStaff
        fields = ['product_name', 'category', 'order_quantity', 'staff', 'order_date']      