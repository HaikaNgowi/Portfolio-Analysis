age=19
if age >= 18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")
else:
	print("Sorry, You are too young to vote!")
	print("Please register to vote as soon as you turn 18!")

#Amusement Park.py
# Different charges for different age groups at the park could be coded as follows:
age = 12
if age < 4:
	print("\nYour admission cost is $0.00")
elif age < 18:
	print("\nYour admission cost is $25.00")
else:
	print("\nYour admission cost is $40.00")
#More efficiently above code can be written as:
age = 17
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
print(f"\nYour admission cost is ${price}.")

## else not always necessary, use elif to highlight the group of interest.

# Testing multiple conditions with if statements
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("\nSorry, we are out of green peppers right now.")
	else:
		print(f"\nAdding {requested_topping}.")
print(f"\nFinished making your pizza!")


##checking if a list is not empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

