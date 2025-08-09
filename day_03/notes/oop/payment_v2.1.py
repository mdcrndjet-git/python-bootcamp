class Payment:
    def __init__(self,amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0
"""
# Informal Polymorphism Option
class Coupon:
    def __init__(self,amount,expired):
        self.amount = amount
        self.expired = expired

    def valid(self):
        return not self.expired and self.amount > 0
"""
# Inheritance Polymorphism Option
class Coupon(Payment):
    def __init__(self,amount,expired):
        super().__init__(amount)
        self.expired = expired

        def valid(self):
            return not self.expired and super().valid() > 0

class OnlinePayment:
    def __init__(self,amount,email):
        self.amount = amount
        self.email = email

    def valid(self):
        isvalid = self.email.endswith('@gmail.com')
        isvalid = isvalid and self.amount > 0
        return isvalid

class CardPayment(Payment):
    def __init__(self,amount,card_number):
        super().__init__(amount)
        self.card_number = card_number

    def valid(self):
        isvalid = self.card_number.isnumeric()               # is number
        isvalid = isvalid and len(self.card_number) == 16    # is 16 digit
        isvalid = isvalid and super().valid()
        return isvalid