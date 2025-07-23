# Fill in the details of the item you plan to buy
item = {
    "Name": "Macbook Pro M4",
    "Info": "2025 Model",
    "Price": 100_000
}

# Print the item details
print("Item:")
for detail_name, detail_value in item.items():
    print(f"\t{detail_name}:\t{detail_value}")
