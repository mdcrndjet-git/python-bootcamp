# list tuple /tuple list

# tuple
items = ("a","b","c")
others = (1,2,3)

for others, item in zip(items, others):
    print("Item",item)
    print("Other",others)