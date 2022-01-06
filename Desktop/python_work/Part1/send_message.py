##Preventing a function from modifying a list
##Sending a copy of a list to a function:
##function_name(list_name[:])

##Passing an arbitrary number of arguments pizza.py;*create empty tupple
def make_pizza(*toppings):
	"""print the list of toppings that have been requested."""
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f" -{topping}")
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushroms', 'green peppers', 'extra cheese')

##Mixing positional and arbitrary arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',
						location='princeton',
						field='physics')
print(user_profile)

##*collects arbitrary positional arguments;**collect non-specific keyword arguments

###Storing functions in modules: allows u to use others functions and also store your own
##importing an entire module - see make_pizzas
##importing specific functions from a module [from module_name import function_name(function_0, function_2 etc)]- see make_pizzas

##Using as to give a function an alias; alias for make_pizza() is mp() - import make_pizza as mp

#using as to give a module an alias: alias for pizza is p - import pizza as p - see make_pizza

##import all functions in a module - * from module_name import *

#Styling functions

















