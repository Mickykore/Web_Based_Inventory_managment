from django.shortcuts import render, redirect
from django.http import HttpResponse
from .reports import *
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Sales
from .form import ProductForm, CategoryForm, SalesForm
import itertools
from datetime import datetime
@login_required(login_url='/login/')
def home(request):
    
    return render(request, 'dashboard/home.html')
    # return HttpResponse('<h1>Home page</h1>')
    
    
@login_required(login_url='/login/')
def product(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        products = Product.objects.filter(category__category=selected_category)
    else:
        products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
        add_categories = CategoryForm(request.POST)
        if add_categories.is_valid():
            add_categories.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
        add_categories = CategoryForm()
    context = {
        'products': products,
        'form': form,
        'categories': categories,
        'selected_category': selected_category,
        'add_categories': add_categories,
    }
    return render(request, 'dashboard/product.html', context)


# @login_required(login_url='/login/')
# def report(request):
#     return render(request, 'dashboard/report.html')

# @login_required(login_url='/login/')
# def reports(request):
#     daily_sales, total_sales = get_daily_sales()  # Get daily sales report

#     daily_sales_data = []
#     total_profit = 0

#     for sale in daily_sales:
#         sale_data = {
#             'product_name': sale.product_name.name,
#             'product_category': sale.product_name.category.category,
#             'purchased_price': sale.product_name.price,
#             'sale_price': sale.sale_price,
#             'quantity': sale.sale_quantity,
#         }
#         sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
#         sale_data['total_sale'] = sale_data['sale_price'] * sale_data['quantity']
#         sale_data['total_profit'] = sale_data['profit'] * sale_data['quantity']
#         daily_sales_data.append(sale_data)

#         total_profit += sale_data['total_profit']

#     context = {
#         'daily_sales': daily_sales_data,
#         'total_sales': total_sales,
#         'total_profit': total_profit,
#     }
#     return render(request, 'dashboard/report.html', context)

@login_required(login_url='/login/')

def reports(request):
    filter_type = request.GET.get('filter', 'daily')  # Get the filter type from the query parameters
    selected_date = request.GET.get('date')  # Get the selected date from the query parameters

    if filter_type == 'daily':
        # Get daily sales report for the selected date or today if no date is selected
        if selected_date:
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            daily_sales, total_daily_sales = get_daily_sales(date)
        else:
            daily_sales, total_daily_sales = get_daily_sales()
        weekly_sales, total_weekly_sales = get_weekly_sales()
        monthly_sales, total_monthly_sales = get_monthly_sales()
        yearly_sales, total_yearly_sales = get_yearly_sales()
    elif filter_type == 'weekly':
        # Get weekly sales report for the selected date range or the current week if no date range is selected
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            weekly_sales, total_weekly_sales = get_weekly_sales(start_date)
        else:
            weekly_sales, total_weekly_sales = get_weekly_sales()
        daily_sales, total_daily_sales = get_daily_sales()
        monthly_sales, total_monthly_sales = get_monthly_sales()
        yearly_sales, total_yearly_sales = get_yearly_sales()
    elif filter_type == 'monthly':
        # Get monthly sales report for the selected month and year or the current month and year if no date is selected
        if selected_date:
            date = datetime.strptime(selected_date, '%Y-%m').date()
            monthly_sales, total_monthly_sales = get_monthly_sales(date)
        else:
            monthly_sales, total_monthly_sales = get_monthly_sales()
        daily_sales, total_daily_sales = get_daily_sales()
        weekly_sales, total_weekly_sales = get_weekly_sales()
        yearly_sales, total_yearly_sales = get_yearly_sales()
    elif filter_type == 'yearly':
        # Get yearly sales report for the selected year or the current year if no date is selected
        if selected_date:
            date = datetime.strptime(selected_date, '%Y').date()
            yearly_sales, total_yearly_sales = get_yearly_sales(date)
        else:
            yearly_sales, total_yearly_sales = get_yearly_sales()
        daily_sales, total_daily_sales = get_daily_sales()
        weekly_sales, total_weekly_sales = get_weekly_sales()
        monthly_sales, total_monthly_sales = get_monthly_sales()
    else:
        # Get all sales data
        daily_sales, total_daily_sales = get_daily_sales()
        weekly_sales, total_weekly_sales = get_weekly_sales()
        monthly_sales, total_monthly_sales = get_monthly_sales()
        yearly_sales, total_yearly_sales = get_yearly_sales()

    daily_sales_data = []
    weekly_sales_data = []
    monthly_sales_data = []
    yearly_sales_data = []
    total_daily_profit = 0
    total_daily_sale_amount = 0  # Add a variable to keep track of the total sales amount
    total_weekly_profit = 0
    total_weekly_sale_amount = 0
    total_monthly_profit = 0
    total_monthly_sale_amount = 0
    total_yearly_profit = 0
    total_yearly_sale_amount = 0

    for sale in daily_sales:
        sale_data = {
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_daily_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_daily_profit'] = sale_data['profit'] * sale_data['quantity']
        daily_sales_data.append(sale_data)

        total_daily_profit += sale_data['total_daily_profit']
        total_daily_sale_amount += sale_data['total_daily_sale_amount']  # Increment the total sales amount

    for sale in weekly_sales:
        sale_data = {
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_weekly_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_weekly_profit'] = sale_data['profit'] * sale_data['quantity']
        weekly_sales_data.append(sale_data)
        
        total_weekly_profit += sale_data['total_weekly_profit']
        total_weekly_sale_amount += sale_data['total_weekly_sale_amount']

    for sale in monthly_sales:
        sale_data = {
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_monthly_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_monthly_profit'] = sale_data['profit'] * sale_data['quantity']
        monthly_sales_data.append(sale_data)
        
        total_monthly_profit += sale_data['total_monthly_profit']
        total_monthly_sale_amount += sale_data['total_monthly_sale_amount']

    for sale in yearly_sales:
        sale_data = {
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_yearly_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_yearly_profit'] = sale_data['profit'] * sale_data['quantity']
        yearly_sales_data.append(sale_data)
        
        total_yearly_profit += sale_data['total_yearly_profit']
        total_yearly_sale_amount += sale_data['total_yearly_sale_amount']

    # Prepare the context to pass to the template
    context = {
        'daily_sales': daily_sales_data,
        'total_daily_sales': total_daily_sales,
        'weekly_sales': weekly_sales_data,
        'total_weekly_sales': total_weekly_sales,
        'monthly_sales': monthly_sales_data,
        'total_monthly_sales': total_monthly_sales,
        'yearly_sales': yearly_sales_data,
        'total_yearly_sales': total_yearly_sales,
        'filter_type': filter_type,
        'selected_date': selected_date,
        'total_daily_profit': total_daily_profit,
        'total_daily_sale_amount': total_daily_sale_amount,  # Add the total sales amount to the context
        'total_weekly_profit': total_weekly_profit,
        'total_weekly_sale_amount': total_weekly_sale_amount,
        'total_monthly_profit': total_monthly_profit,
        'total_monthly_sale_amount': total_monthly_sale_amount,
        'total_yearly_profit': total_yearly_profit,
        'total_yearly_sale_amount': total_yearly_sale_amount,
    }

    return render(request, 'dashboard/report.html', context)


@login_required(login_url='/login/')
def sales(request):
    sales = Sales.objects.all()
    daily_sales, total_daily_sales = get_daily_sales()
    daily_sales_data = []
    total_profit = 0
    total_sale_amount = 0 
    id_obj = itertools.count()
    sale_date = Sales.sale_date
    for sale in daily_sales:
        sale_data = {
            'ID': next(id_obj),
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
        total_sale_amount += sale_data['total_sale']  # Increment the total sales amount


    if request.method == 'POST':
        sales_form = SalesForm(request.POST)
        if sales_form.is_valid():
            sales_form.save()
            return redirect('dashboard-sales')
    else:
        sales_form = SalesForm()
    context = {
        'sales': sales,
        'sales_form':sales_form,
        'daily_sales': daily_sales_data,
        'total_daily_sales': total_daily_sales,
        'total_profit': total_profit,
        'total_sale_amount': total_sale_amount,
        'sale_date': sale_date,
    }
    return render(request, 'dashboard/sales.html', context)
