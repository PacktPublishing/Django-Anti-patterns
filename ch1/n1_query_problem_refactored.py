# Optimized version using select_related

for order in Order.objects.select_related("item").all():

    print(
        order.item.name
    )  # Item details are fetched in a single query along with orders
