from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='dashboard_home'),
    path('reports/', views.reports, name='dashboard-reports'),
    path('product/', views.product, name='dashboard-product'),
]