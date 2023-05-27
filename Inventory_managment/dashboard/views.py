from django.shortcuts import render
from django.http import HttpResponse
from .reports import *
def home(request):
    return render(request, 'dashboard/home.html')
    # return HttpResponse('<h1>Home page</h1>')
def product(request):
    return render(request, 'dashboard/product.html')

def sales(request):
    return render(request, 'dashboard/sales.html')

def report(request):
    return render(request, 'dashboard/report.html')


def reports(request):
    daily_sales = get_daily_sales()
    weekly_sales = get_weekly_sales()
    monthly_sales = get_monthly_sales()
    yearly_sales = get_yearly_sales()
    # You can retrieve more data or perform additional calculations here
    context = {
        'daily_sales': daily_sales,
        'weekly_sales': weekly_sales,
        'monthly_sales': monthly_sales,
        'yearly_sales': yearly_sales
    }
    return render(request, 'dashboard/report.html', context)