import json

def clean_filepath(string):
    string = string.strip()

    return string

def create(inventory, item):
    """Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)

def read(inventory, index):
    """Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]

def update(inventory, index, detail_key, detail_value):
    """Change/add the key and value to the given index in inventory"""
    inventory_record = inventory[index]
    inventory_record[detail_key] = detail_value

def delete(inventory, index):
    """Remove item (dict) in the given index (int) of inventory"""
    del inventory[index]

def show(inventory):
    """Print the items and their details line-by-line"""
    print("Item: ", inventory)
    for item in inventory:
        for key, value in item.items():
            print(f"\t{key}: {value}")

def save(inventory, filepath):
    # Save the inventory in the filepath in JSON format
    inventory_file = filepath +"\\inventory.json"
    with open(inventory_file, "w") as file:
        json.dump(inventory, file)

def load(filepath):
    # Save the inventory in the filepath in JSON format
    inventory_file = filepath +"\\inventory.json"
    with open(inventory_file, "r") as file:
        data = json.load(file)

    return data

def main():
    current_inventory = []
    command = input("Command: ")

    while command:
        # Handle command here
        # Ask the inputs here, not in the function
        if command == "create":
            item_name = input("Item name: ")
            item = {"Name": item_name}
            create(current_inventory,item)

        elif command == "read":
            index = int(input("Item index: "))
            read(current_inventory, index)

        elif command == "update":
            index = int(input("Item index: "))
            item_key = input("Item key: ")
            item_value = input("Item new value: ")
            update(current_inventory, index, item_key, item_value)

        elif command == "save":
            filepath_input = input("Save to file: ")
            filepath_input = clean_filepath(filepath_input)
            save(current_inventory, filepath_input)
            print("Done saving to file.")

        elif command == "load":
            filepath_input = input("Load file: ")
            filepath_input = clean_filepath(filepath_input)
            current_inventory = load(filepath_input)
            print("Done loading file.")

        elif command == "delete":
            index = int(input("Item index: "))
            delete(current_inventory, index)

        elif command == "show":
            show(current_inventory)

        # Ask for more
        command = input("Command: ")


main()
