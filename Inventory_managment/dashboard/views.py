from django.shortcuts import render
from django.http import HttpResponse
from .reports import *
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def home(request):
    return render(request, 'dashboard/home.html')
    # return HttpResponse('<h1>Home page</h1>')
@login_required(login_url='/login/')
def product(request):
    return render(request, 'dashboard/product.html')

@login_required(login_url='/login/')
def sales(request):
    return render(request, 'dashboard/sales.html')

@login_required(login_url='/login/')
def report(request):
    return render(request, 'dashboard/report.html')

@login_required(login_url='/login/')
def reports(request):
    daily_sales, total_sales = get_daily_sales()  # Get daily sales report

    daily_sales_data = []
    total_profit = 0

    for sale in daily_sales:
        sale_data = {
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_sale'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_profit'] = sale_data['profit'] * sale_data['quantity']
        daily_sales_data.append(sale_data)

        total_profit += sale_data['total_profit']

    context = {
        'daily_sales': daily_sales_data,
        'total_sales': total_sales,
        'total_profit': total_profit,
    }
    return render(request, 'dashboard/report.html', context)
def reports(request):
    daily_sales, total_daily_sales = get_daily_sales()  # Get daily sales report
    weekly_sales, total_weekly_sales = get_weekly_sales()  # Get weekly sales report
    monthly_sales, total_monthly_sales = get_monthly_sales()  # Get monthly sales report
    yearly_sales, total_yearly_sales = get_yearly_sales()  # Get yearly sales report

    daily_sales_data = []
    total_profit = 0

    for sale in daily_sales:
        sale_data = {
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_sale'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_profit'] = sale_data['profit'] * sale_data['quantity']
        daily_sales_data.append(sale_data)

        total_profit += sale_data['total_profit']

    context = {
        'daily_sales': daily_sales_data,
        'total_daily_sales': total_daily_sales,
        'weekly_sales': weekly_sales,
        'total_weekly_sales': total_weekly_sales,
        'monthly_sales': monthly_sales,
        'total_monthly_sales': total_monthly_sales,
        'yearly_sales': yearly_sales,
        'total_yearly_sales': total_yearly_sales,
        'total_profit': total_profit,
    }
    return render(request, 'dashboard/report.html', context)
