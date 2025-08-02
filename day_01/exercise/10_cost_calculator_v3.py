# Ask the user how many items to purchase
item_count = int(input("Item count: "))
total = 0

# For every item in range of item_count, ask for an item price
for item in range(item_count):
    # zero padding in item index text
    item_price = int(input(f"{item +1:0>2} - Enter item price: "))

    #Add the item price to the total price
    total = total +item_price

print("Total:",total)
