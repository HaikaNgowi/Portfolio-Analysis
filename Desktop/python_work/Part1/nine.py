##modules < classes < instances aka objects <classes - classes>
#Creating the dog class

class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} roll over!")
##Making an instance from a class
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Accessing attributes
my_dog.name

#Calling method
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

#Creating multiple instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

































