class Item:
    def __init__(self, name, price, quantity, details):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.details = details

    def total_cost(self):
        return self.price * self.quantity

    def as_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "details": self.details,
        }


class Inventory:

    def __init__(self):
        self.items = []

    def create(self, item):
        """Add a new item (dict) to the inventory (list[dict])"""

    def read(self, index):
        """Return the item (dict) in the given index (int) of inventory"""

    def delete(self, index):
        """Remove item (dict) in the given index (int) of inventory"""

    def show(self):
        """Print the items and their details line-by-line"""

    def save(self, filepath):
        """Save the inventory (list[dict]) to a filepath"""

    def load(self, filepath):
        """Return a list[dict] from a filepath"""


def main():
    inventory = Inventory()
    command = input("Command: ")

    while command:
        # Handle command here
        # Ask the inputs here, not in the function

        # Ask for more
        command = input("Command: ")


main()
