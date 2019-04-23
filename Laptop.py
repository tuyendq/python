class Laptop(object):
	def __init__(self, make, model):
		self.make = make
		self.model = model

	def info(self):
		print self.make, " ", self.model

first_lt = Laptop("Asus", "J73Gh")
second_lt = Laptop("Lenovo", "T420")

first_lt.info()
second_lt.info()
