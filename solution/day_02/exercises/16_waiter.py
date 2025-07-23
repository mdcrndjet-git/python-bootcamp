orders = {}

order = input("Enter order: ")
while order:
    count = int(input("Enter how many: "))

    if order in orders:
        orders[order] += count
    else:
        orders[order] = count

    order = input("Enter order: ")
print(orders)
