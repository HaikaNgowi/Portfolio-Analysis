# Specific groups of elements in a list - slices
# Players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[1:4])
print(players[1:])
print(players[:-3])
print(players[-2:])
print("\nHere are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# Copying lists
#Foods.py
my_foods = ['pizza', 'ugali', 'beans', 'cereal', 'sukuma']
friends_foods = my_foods [:]
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friends favorite foods are:")
print(friends_foods)
my_foods = friends_foods
print(friends_foods)
my_foods.append('cream')
friends_foods.append('cheese')
print(my_foods)
print(friends_foods)
print("\nThe first three items in the list are:")
print(my_foods[:3])
print("\nThe three middle items in the list are:")
print(my_foods[1:-3])
print("\nThe last three items in the list are:")
print(my_foods[2:-2])
my_pizza = ['pepperoni', 'hawaii', 'cheese', 'vegan']
friends_pizza = my_pizza [:]
print("\nMy favorite pizzas are:")
print(my_pizza)
print("\nMy friends favorite pizzas are:")
print(friends_pizza)
my_pizza.append('chicken')
friends_pizza.append('olive')
print("\nMy favorite pizzas are:")
print(my_pizza)
my_pizza = ['pepperoni', 'hawaii', 'cheese', 'vegan', 'chicken']
for pizzas in my_pizza[5:]:
	print(my_pizza)
print("\nMy friends favorite pizzas are:")
my_pizza = friends_pizza [:]
print(friends_pizza)
friends_pizza = ['pepperoni', 'hawaii', 'cheese', 'vegan', 'olive']
for pizzas in friends_pizza[5:]:
	print(friends_pizza)
print(my_pizza)

#the added pizza in my pizza doesnt show after printng both lists - investigate.

