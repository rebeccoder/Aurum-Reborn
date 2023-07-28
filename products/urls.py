from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<str:sku>/', views.product_detail, name='product_detail'),
    path('edit/<str:product_sku>/', views.edit_product, name='edit_product'),
    path('delete/<str:product_sku>/', views.delete_product, name='delete_product'),
]