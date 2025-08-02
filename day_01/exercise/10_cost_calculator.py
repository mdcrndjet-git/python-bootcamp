# Ask the user for the following inputs
item_1_price = float(input("Item price 1: "))
item_2_price = float(input("Item price 2: "))
item_3_price = float(input("Item price 3: "))

# Print: Total cost
total = None
total = round(item_1_price +item_2_price +item_3_price, 2)
print(total)
