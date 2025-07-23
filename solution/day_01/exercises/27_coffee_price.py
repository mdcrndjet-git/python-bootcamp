def coffee_price(kind, size, has_discount):
    """
    Returns the final price with the following scheme:
        Base Price: Americano (100), Latte (110), Cappuccino (120)
        Size Multiplier: Small (x0.8), Medium  (x1.0), Large (x1.2)
        Has Discount: x0.88 (removed VAT)
    """
    base_price = 0
    if kind == "Americano":
        base_price = 100
    elif kind == "Latte":
        base_price = 110
    elif kind == "Cappuccino":
        base_price = 120

    multiplier = 0
    if size == "small":
        multiplier = 0.8
    elif size == "medium":
        multiplier = 1.0
    elif size == "large":
        multiplier = 1.2

    discount_multiplier = 0
    if has_discount:
        discount_multiplier = 0.88
    else:
        discount_multiplier = 1.0

    return discount_multiplier * base_price * multiplier


print(coffee_price("Latte", "Large", True))
print(coffee_price("Americano", "Small", False))
