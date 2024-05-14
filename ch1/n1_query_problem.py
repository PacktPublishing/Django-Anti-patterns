# Example of an N+1 query problem in Django

for order in Order.objects.all():

    print(order.item.name)  # Each iteration hits the database again to get item details