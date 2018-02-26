class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self, tax):
		return self.price * (1 + tax)

	def return_product(self, reason):
		if reason.lower() == "defective":
			self.price = 0
			self.status = "Defective"
		elif reason.lower() == "like new":
			self.status = "for sale"
		elif reason.lower() == "open":
			self.status = "used"
			self.price *= 0.8

		return self

	def display_info(self):
		print "Item Name: {}".format(self.item_name)
		print "Price: {}".format(self.price)
		print "Weight: {}".format(self.weight)
		print "Brand: {}".format(self.brand)
		print "Status: {}".format(self.status)

		return self


def new_product(price, item_name, weight, brand):
	return Product(price, item_name, weight, brand)