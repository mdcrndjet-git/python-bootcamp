# Ask the user for the following inputs
item_1_price = int(input("Enter item 1 price: "))
item_1_quantity = int(input("Enter item 1 quantity: "))

item_2_price = int(input("Enter item 2 price: "))
item_2_quantity = int(input("Enter item 2 quantity: "))

item_3_price = int(input("Enter item 3 price: "))
item_3_quantity = int(input("Enter item 3 quantity: "))

# Print: Total Cost
total = (
        item_1_price * item_1_quantity
        + item_2_price * item_2_quantity
        + item_3_price * item_3_quantity
)
print(total)
