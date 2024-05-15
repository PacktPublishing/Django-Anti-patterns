# Bad practice: Fat view handling too much logic
def order_summary(request):
    user = request.user
    orders = user.orders.all()
    total_amount = sum(order.total_amount for order in orders)
    return render(request, 'orders/summary.html', {'orders': orders, 'total_amount': total_amount})