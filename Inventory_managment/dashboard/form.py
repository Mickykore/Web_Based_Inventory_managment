from django import forms
from .models import Product, Category, Sales

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
        