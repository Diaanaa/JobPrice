class Good:

	def __init__(self, name, price, exempt = False):
		self.name = name
		self.price = price
		self.exempt = exempt

	def price_after_taxation(self):
		if self.exempt == "exempt":
			price_of_good = self.price*1.07
		else:
			price_of_good = self.price
		return price_of_good

	def __str__(self):
		return self.name + ": %" + round(price_after_taxation(self.price),2)