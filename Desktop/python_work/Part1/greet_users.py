def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#Modifying a list in a function
##Start with designs that need to be printing
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

##Simulate printing each design until none are left; move each design to completed models after printing
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)
##Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

##reorganize above code into two parts
##1. 
def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until nne are left.
	Move each design to completed_models after printing.
	"""
while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

##2. 
def show_completed_models(completed_models):
	"""show all models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

##copy list into function
print_models(unprinted_designs[:], completed_models)




