from .models import Product, Sales, Category
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

def get_daily_sales():
    today = timezone.now().date()
    daily_sales = Sales.objects.filter(sale_date__date=today).aggregate(total_sales=Sum('sale_price'))
    return daily_sales['total_sales']

def get_weekly_sales():
    start_of_week = timezone.now().date() - timedelta(days=timezone.now().date().weekday())
    end_of_week = start_of_week + timedelta(days=6)
    weekly_sales = Sales.objects.filter(sale_date__date__range=[start_of_week, end_of_week]).aggregate(total_sales=Sum('sale_price'))
    return weekly_sales['total_sales']

def get_monthly_sales():
    current_month = timezone.now().date().month
    monthly_sales = Sales.objects.filter(sale_date__month=current_month).aggregate(total_sales=Sum('sale_price'))
    return monthly_sales['total_sales']

def get_yearly_sales():
    current_year = timezone.now().date().year
    yearly_sales = Sales.objects.filter(sale_date__year=current_year).aggregate(total_sales=Sum('sale_price'))
    return yearly_sales['total_sales']
