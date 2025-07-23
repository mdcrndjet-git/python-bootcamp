wishlist = [
    {
        "Name": "Macbook Pro M4",
        "Info": "2025 Model",
        "Price": 100_000
    },
    {
        "Name": "Laptop Stand",
        "Info": "U Green Aluminum",
        "Price": 2_000
    },

]

print("Wishlist:")
for index, item in enumerate(wishlist, start=1):

    print(f"Item {index}:")
    for detail_name, detail_value in item.items():
        print(f"\t{detail_name}:\t{detail_value}")
