# Bad practice: Inefficient queryset
def get_recent_orders(request):
    # Inefficient queryset: N + 1 queries
    orders = Order.objects.all()
    for order in orders:
        print(order.customer.name)  # Causes an additional query for each order
    return render(request, 'orders/recent_orders.html', {'orders': orders})
