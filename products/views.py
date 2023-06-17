from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """ A View to show all products including sorting and search queries """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, sku):
    """ A view to show individual product details """
    product = get_object_or_404(Product, sku=sku)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
