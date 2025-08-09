class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0

class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return not self.expired and super().valid()
