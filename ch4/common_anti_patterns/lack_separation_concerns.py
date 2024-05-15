# Bad practice: Mixing business logic and view logic
def send_order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    # Business logic
    send_email(order.customer.email, 'Order Confirmation', 'Your order has been confirmed.')
    # View logic
    return HttpResponse('Confirmation email sent.')
