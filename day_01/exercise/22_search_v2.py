items = ["rice","noodles","toyo","spam","coffee"]
item_to_find = "egg"

for item in items:
    """
    If item equals the items_to_find, print and exit loop
    """
    print("searching...")
    if item == item_to_find:
        print("Item",item_to_find,"is found.")
        break
else:
    print("Item",item_to_find,"is not found")
