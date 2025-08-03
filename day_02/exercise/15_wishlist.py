# Fill in the details of the item you plan to buy
item = {
    "Name":"Rock",
    "Info":"500 damage"
}

# Print the item details in the following format
"""
Item:
    Name: item name
    Info: item info
"""
print("Item:")
for key, value in item.items():
    print(f"\t{key}: {value}")
