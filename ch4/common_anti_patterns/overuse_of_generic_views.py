# Bad practice: Using generic view for complex logic
class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    queryset = Order.objects.filter(status='pending')  # Overriding queryset can be problematic
