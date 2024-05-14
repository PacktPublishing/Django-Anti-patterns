# Bad practice: Duplicating code
def calculate_discount_price(product):
    if product.category == 'Electronics':
        discount = 0.1
    elif product.category == 'Clothing':
        discount = 0.2
    else:
        discount = 0

    return product.price * (1 - discount)

# Good practice: Using a mapping
CATEGORY_DISCOUNT_MAPPING = {
    'Electronics': 0.1,
    'Clothing': 0.2,
}

def calculate_discount_price(product):
    discount = CATEGORY_DISCOUNT_MAPPING.get(product.category, 0)
    return product.price * (1 - discount)