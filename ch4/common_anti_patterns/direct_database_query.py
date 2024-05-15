# Bad practice: Direct database query in view
def get_user_orders(request):
    user_id = request.GET.get('user_id')
    # Direct database query
    orders = Order.objects.raw(f"SELECT * FROM orders_order WHERE user_id = {user_id}")
    return render(request, 'orders/user_orders.html', {'orders': orders})
