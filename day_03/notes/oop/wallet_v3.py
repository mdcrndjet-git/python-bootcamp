class Wallet:
	def __init__(self, initial_amount=0):
		self.amount = initial_amount

food_wallet = Wallet(250)

#amount is a protected variable
#food_wallet.amount += 1000
#print("Wallet amount:", food_wallet._amount)
