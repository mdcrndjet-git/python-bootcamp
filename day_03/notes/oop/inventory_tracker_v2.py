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
