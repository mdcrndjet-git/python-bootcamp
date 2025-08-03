# Fill in the details of the item you plan to buy
wishlist = [
    {
        "Name": "Rock",
        "Info": "500 damage"
    },
    {
        "Name": "Jose Rizal's Pen",
        "Info": "10000 intelligence"
    },
    {
        "Name": "Jose Rizal's Vest",
        "Info": "500 protection"
    },
    {
        "Name": "Jose Rizal's Hat",
        "Info": "1500 charm"
    },
    {
        "Name": "Manny Pacquiao's Boxing Gloves",
        "Info": "1500 damage"
    },
    {
        "Name": "Manny Pacquiao's Nike Shoes",
        "Info": "2000 speed and 1500 evasion"
    }
]

# Print the item details in the following format
"""
Item:
    Name: item name
    Info: item info
"""
print("Item:")
for wish in wishlist:
    for key, value in wish.items():
        print(f"\t{key}: {value}")
