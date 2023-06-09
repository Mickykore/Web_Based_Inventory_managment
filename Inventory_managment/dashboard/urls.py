from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='dashboard_home'),
    path('reports/', views.reports, name='dashboard-reports'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='dashboard-delete_product'),
    path('product/update/<int:product_id>/', views.update_product, name='dashboard-update_product'),
    path('product/delete_category/<int:category_id>/', views.delete_category, name='dashboard-delete_category'),
    path('product/update_category/<int:category_id>/', views.update_category, name='dashboard-update_category'),
    path('sales/', views.sales, name='dashboard-sales'),
    path('sales/delete/<int:sale_id>/', views.delete_sales, name='dashboard-delete_sales'),
    path('sales/update/<int:sale_id>/', views.update_sales, name='dashboard-update_sales'),
    path('order/', views.order, name='dashboard-orders'),
]