##Working with classes and instances - cars.py
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""Set default value for attribute directly- mileage. add odometer self and add below:"""
		"""Print a statement showing the cars mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set default value for attribute through method."""
		self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#Modifying attributes
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#to make sure no one changes the mileage or rolls it back;
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		"""Set default value for attribute directly- mileage. add odometer self and add below:"""
		"""Print a statement showing the cars mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set odometer reading to set value. reject changes when rolling back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, miles):
		"""Incrementing attribute value through method. add given amount to odometer reading."""
		self.odometer_reading += miles
my_used_car  = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()




















