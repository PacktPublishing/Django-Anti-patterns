MIN_PRICE_FOR_DISCOUNT = 1000

DISCOUNT_RATE = 0.10


def calculate_discount(price):

    if price > MIN_PRICE_FOR_DISCOUNT:

        return price * DISCOUNT_RATE

    return 0