from django.shortcuts import render
from .models import Product

def product_list(request):
    # Anti-pattern: Performing complex database queries directly in views
    # This can lead to performance issues and code duplication
    products = Product.objects.filter(price__gt=100)  # Filter products with price greater than 100
    expensive_products = [p for p in products if p.quantity > 0]  # Further filtering in Python code

    return render(request, 'products/product_list.html', {'products': expensive_products})