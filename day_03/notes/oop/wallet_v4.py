class Wallet:
	def __init__(self, initial_amount=0):
		self._amount = initial_amount

	def get_amount(self):
		return self._amount

	def set_amount(self,amount):
		self._amount = amount

food_wallet = Wallet(250)

#amount is a protected variable
#food_wallet.amount += 1000
#print("Wallet amount:", food_wallet._amount)

food_wallet.set_amount(food_wallet.get_amount() +1000)
print("Wallet amount:", food_wallet.get_amount())
