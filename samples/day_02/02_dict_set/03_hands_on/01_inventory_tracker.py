def create(inventory, item):
    """Add a new item (dict) to the inventory (list[dict])"""


def read(inventory, index):
    """Return the item (dict) in the given index (int) of inventory"""


def update(inventory, index, detail_key, detail_value):
    """Change/add the key and value to the given index in inventory"""


def delete(inventory, index):
    """Remove item (dict) in the given index (int) of inventory"""


def show(inventory):
    """Print the items and their details line-by-line"""


def main():
    current_inventory = []
    command = input("Command: ")

    while command:
        # Handle command here
        # Ask the inputs here, not in the function

        # Ask for more
        command = input("Command: ")


main()
