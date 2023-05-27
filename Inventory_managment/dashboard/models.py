from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.category}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_purchased = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.name} {self.price}'
    
    
class Sales(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(default=timezone.now)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product_name.name} {self.sale_price}'
    
    def save(self, *args, **kwargs):
        # Subtract the sold quantity from the available quantity
        self.product_name.quantity -= self.sale_quantity
        self.product_name.save()  # Save the updated product quantity
        super().save(*args, **kwargs)

    
# class report(models.Model):
#     product_name = models.ForeignKey(Sales, on_delete= models.CASCADE)
#     sale_price = models.ForeignKey(Sales, on_delete= models.CASCADE)
#     sale_date = models.ForeignKey(Sales, on_delete=models.CASCADE)
#     total_sales = models.DecimalField()
    
#     def __str__(self):
#         return f'{self.product_name} {self.sale.price}'
    