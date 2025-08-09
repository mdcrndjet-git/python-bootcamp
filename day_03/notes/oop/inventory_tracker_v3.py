class Item:
    def __init__(self,name,price,quantity,details):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.details = details

        def total_cost(self):
            return self.price *self.quantity

        def as_dict(self):
            return {
                "name": self.name,
                "price": self.price,
                "quantity": self.quantity,
                "details":self.details
            }

class InventoryTracker:
    def __self__(self):
        self.items = []

    def create(self, item):
        self.items.append(item)
        print(f"Created Item: {item.name} - {item.details} - {item.quantity}")

    def read(self, index):
        item = self.items[index]
        print(f"Read Item {index}: {item.name} - {item.details} - {item.quantity}")

    def delete(self, index):
        item = self.items.pop(index)
        print(f"Deleted Item {index}: {item.name} - {item.details} - {item.quantity}")

    def show(self):
        for index,item in enumerate(self.items):
            print(f"Item {index}: {item.name} - {item.details} - {item.quantity}")