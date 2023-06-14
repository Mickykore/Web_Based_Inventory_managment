from django.shortcuts import render, redirect
from .reports import *
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Sales, OrderByCustomer, OrderByStaff
from .form import ProductForm, CategoryForm, SalesForm, CustomerOrderForm, StaffOrderForm
import itertools
from datetime import datetime,date
from django.contrib import messages

@login_required(login_url='/login/')
# Dashboard
def home(request):
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
            name = form.cleaned_data.get('name')
            messages.success(request, f'product {name} added successfully')
            return redirect('dashboard-product')
        add_categories = CategoryForm(request.POST)
        if add_categories.is_valid():
            add_categories.save()
            category = add_categories.cleaned_data.get('category')
            messages.success(request, f'{category} added successfully')
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
    return render(request, 'dashboard/home.html', context)

# Landing Page   
def landing(request):
    return render(request, 'dashboard/Landing/index.html')
# About Page
def about(request):
    return render(request, 'dashboard/Landing/about.html')
# Features Page
def features(request):
    return render(request, 'dashboard/Landing/features.html')
# Contacts Page
def contact(request):
    return render(request, 'dashboard/Landing/contact.html')

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
            name = form.cleaned_data.get('name')
            messages.success(request, f'product {name} added successfully')
            return redirect('dashboard-product')
        add_categories = CategoryForm(request.POST)
        if add_categories.is_valid():
            add_categories.save()
            category = add_categories.cleaned_data.get('category')
            messages.success(request, f'{category} added successfully')
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

@login_required(login_url='/login/')
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('dashboard-product')

    context = {
        'product': product,
    }
    return render(request, 'dashboard/delete_product.html', context)

@login_required(login_url='/login/')
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=product)

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'dashboard/update_product.html', context)
@login_required(login_url='/login/')
def delete_category(request, category_id):
    categories =Category.objects.get(id=category_id)
    if request.method == 'POST':
        categories.delete()
        return redirect('dashboard-product')

    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/delete_category.html', context)

@login_required(login_url='/login/')
def update_category(request, category_id):
    categories = Category.objects.get(id=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=categories)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = CategoryForm(instance=categories)

    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'dashboard/update_category.html', context)



@login_required(login_url='/login/')

def reports(request):
    filter_type = request.GET.get('filter', 'daily')  # Get the filter type from the query parameters
    selected_date = request.GET.get('date')  # Get the selected date from the query parameters
    no = itertools.count()
    # if filter_type == 'daily':
        # Get daily sales report for the selected date or today if no date is selected
    if selected_date:
        date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        daily_sales, total_daily_sales = get_daily_sales(date)
        weekly_sales, total_weekly_sales, start_of_week, end_of_week = get_weekly_sales(date)
        monthly_sales, total_monthly_sales = get_monthly_sales(date)
        yearly_sales, total_yearly_sales = get_yearly_sales(date)
    else:
        daily_sales, total_daily_sales = get_daily_sales()
        weekly_sales, total_weekly_sales, start_of_week, end_of_week = get_weekly_sales()
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
            'no': next(no),
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
            'sale_date': sale.sale_date,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_daily_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_daily_profit'] = sale_data['profit'] * sale_data['quantity']
        daily_sales_data.append(sale_data)

        total_daily_profit += sale_data['total_daily_profit']
        total_daily_sale_amount += sale_data['total_daily_sale_amount']  # Increment the total sales amount
        
    no = itertools.count()
    for sale in weekly_sales:
        sale_data = {
            'no': next(no),
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
            'sale_date': sale.sale_date,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_weekly_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_weekly_profit'] = sale_data['profit'] * sale_data['quantity']
        weekly_sales_data.append(sale_data)
        
        total_weekly_profit += sale_data['total_weekly_profit']
        total_weekly_sale_amount += sale_data['total_weekly_sale_amount']

    no = itertools.count()
    for sale in monthly_sales:
        sale_data = {
            'no': next(no),
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
            'sale_date': sale.sale_date,
        }
        sale_data['profit'] = sale_data['sale_price'] - sale_data['purchased_price']
        sale_data['total_monthly_sale_amount'] = sale_data['sale_price'] * sale_data['quantity']
        sale_data['total_monthly_profit'] = sale_data['profit'] * sale_data['quantity']
        monthly_sales_data.append(sale_data)
        
        total_monthly_profit += sale_data['total_monthly_profit']
        total_monthly_sale_amount += sale_data['total_monthly_sale_amount']

    no = itertools.count()
    for sale in yearly_sales:
        sale_data = {
            'no': next(no),
            'product_name': sale.product_name.name,
            'product_category': sale.product_name.category.category,
            'purchased_price': sale.product_name.price,
            'sale_price': sale.sale_price,
            'quantity': sale.sale_quantity,
            'sale_date': sale.sale_date,
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
        'end_of_week': end_of_week,
        'start_of_week': start_of_week,
        
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
            'sale_date': sale.sale_date,
            'id': sale.id,
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
            sale_price = sales_form.cleaned_data['sale_price']
            purchased_price = sales_form.cleaned_data['product_name'].price
            sale_quantity = sales_form.cleaned_data['sale_quantity']
            product_quantity = sales_form.cleaned_data['product_name'].quantity
            
            if sale_price < purchased_price:
                sales_form.add_error('sale_price', 'Sale price cannot be less than purchased price.')
            
            if sale_quantity > product_quantity:
                sales_form.add_error('sale_quantity', 'Sale quantity cannot be greater than the product quantity.')
            
            if not sales_form.errors:
                sales_form.save()
                return redirect('dashboard-sales')
    else:
        sales_form = SalesForm()
    
    context = {
        'sales': sales,
        'sales_form': sales_form,
        'daily_sales': daily_sales_data,
        'total_daily_sales': total_daily_sales,
        'total_profit': total_profit,
        'total_sale_amount': total_sale_amount,
        'sale_date': sale_date,
    }
    return render(request, 'dashboard/sales.html', context)


@login_required(login_url='/login/')
def delete_sales(request, sale_id):
    sale = Sales.objects.get(id=sale_id)

    if request.method == 'POST':
        sale.delete()
        return redirect('dashboard-sales')

    context = {
        'sale': sale,
    }
    return render(request, 'dashboard/delete_sales.html', context)

@login_required(login_url='/login/')
def update_sales(request, sale_id):
    sale = Sales.objects.get(id=sale_id)

    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('dashboard-sales')
    else:
        form = SalesForm(instance=sale)

    context = {
        'sale': sale,
        'form': form,
    }
    return render(request, 'dashboard/update_sales.html', context)

@login_required(login_url='/login/')
def order(request):
    customer_orders = OrderByCustomer.objects.all()
    staff_orders = OrderByStaff.objects.all()
    low_quantity_products = Product.objects.filter(quantity__lte=5)
    if request.method == 'POST':
        customer_form = CustomerOrderForm(request.POST)
        staff_form = StaffOrderForm(request.POST)
        
        if 'customer_order' in request.POST and customer_form.is_valid():
            customer_form.save()
            return redirect('dashboard-orders')
        
        if 'staff_order' in request.POST and staff_form.is_valid():
            staff_form.save()
            return redirect('dashboard-orders')

    else:
        customer_form = CustomerOrderForm()
        staff_form = StaffOrderForm()

    context = {
        'customer_form': customer_form,
        'staff_form': staff_form,
        'customer_orders': customer_orders,
        'staff_orders': staff_orders,
        'low_quantity_products': low_quantity_products,
    }
    return render(request, 'dashboard/order.html', context)

@login_required(login_url='/login/')
def delete_customer_order(request, order_id):
    customer_orders = OrderByCustomer.objects.get(id=order_id)
    if request.method == 'POST':  
            customer_orders.delete()
            return redirect('dashboard-orders')

    context = {
        'customer_orders': customer_orders,
    }
    return render(request, 'dashboard/delete_customer_order.html', context)
@login_required(login_url='/login/')
def delete_staff_order(request, order_id):
    staff_orders = OrderByStaff.objects.get(id=order_id)
    if request.method == 'POST':  
            staff_orders.delete()
            return redirect('dashboard-orders')


    context = {
        'staff_orders': staff_orders,
    }
    return render(request, 'dashboard/delete_staff_order.html', context)

@login_required(login_url='/login/')
def update_customer_order(request, order_id):
    customer_order = OrderByCustomer.objects.get(id=order_id)

    if request.method == 'POST':
        customer_form = CustomerOrderForm(request.POST, instance=customer_order)
        
        if customer_form.is_valid():
            customer_form.save()
            return redirect('dashboard-orders')

    else:
        customer_form = CustomerOrderForm(instance=customer_order)

    context = {
        'customer_form': customer_form,
        'customer_orders': customer_order,
    }
    return render(request, 'dashboard/update_customer_order.html', context)
def update_staff_order(request, order_id):
    staff_order = OrderByStaff.objects.get(id=order_id)

    if request.method == 'POST':
        staff_form = StaffOrderForm(request.POST, instance=staff_order)
        
        if staff_form.is_valid():
            staff_form.save()
            return redirect('dashboard-orders')

    else:
        staff_form = StaffOrderForm(instance=staff_order)

    context = {
        'staff_form': staff_form,
        'staff_orders': staff_order,
    }
    return render(request, 'dashboard/update_staff_order.html', context)