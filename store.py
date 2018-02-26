from product import new_product

class Store(object):
	def __init__(self, location, owner):
		self.products = []
		self.location = location
		self.owner = owner

	def add_product(self, product):
		self.products.append(product)
		return self

	def remove_product(self, product):
		self.products.remove(product)
		return self

	def inventory(self):
		for product in self.products:
			print product.display_info()
			print " "
		return self


# Product(price, item_name, weight, brand)
store1 = Store("123 Sesame Street", "Daniel Clancy")

product1 = new_product(5, "Cookies", "16oz", "Oreo")
product2 = new_product(10, "Chicken", "2lbs", "Perdue")

print "adding products"
store1.add_product(product1).add_product(product2)

print "Inventory"
store1.inventory()


print "Removing a product"
store1.remove_product(product1)


print "Inventory"
store1.inventory()