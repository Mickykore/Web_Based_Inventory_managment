from .models import Product, Sales, Category
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

def get_daily_sales():
    today = timezone.localtime().date()  # Convert to the local timezone
    daily_sales = Sales.objects.filter(sale_date__date=today)
    total_sales = daily_sales.aggregate(total_sales=Sum('sale_price'))['total_sales']
    return daily_sales, total_sales

def get_weekly_sales():
    start_of_week = timezone.localtime().date() - timedelta(days=timezone.localtime().date().weekday())
    end_of_week = start_of_week + timedelta(days=6)
    weekly_sales = Sales.objects.filter(sale_date__date__range=[start_of_week, end_of_week])
    total_sales = weekly_sales.aggregate(total_sales=Sum('sale_price'))['total_sales']
    return weekly_sales, total_sales

def get_monthly_sales():
    current_month = timezone.localtime().date().month
    monthly_sales = Sales.objects.filter(sale_date__month=current_month)
    total_sales = monthly_sales.aggregate(total_sales=Sum('sale_price'))['total_sales']
    return monthly_sales, total_sales

def get_yearly_sales():
    current_year = timezone.localtime().date().year
    yearly_sales = Sales.objects.filter(sale_date__year=current_year)
    total_sales = yearly_sales.aggregate(total_sales=Sum('sale_price'))['total_sales']
    return yearly_sales, total_sales



