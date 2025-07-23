# Ask the user how many items to purchase
item_count = int(input("Enter item count: "))
total = 0

# For every item in range of item_count, ask for an item price
for _ in range(item_count):
    item_price = int(input("Enter item count: "))
    item_quantity = int(input("Enter item quantity: "))

    # Add the item price to the total price
    total += (item_price * item_quantity)

print(total)
