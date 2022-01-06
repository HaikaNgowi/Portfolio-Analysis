#storage of multiple dictionaries in a list
alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

#Make an empty alien list then make 30 green aliens then show the first 5
aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}.")

#A list in a dictionary
# Information of toppings on pizza
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}- crust pizza "
	"with the following toppings:")
for topping in pizza['toppings']:
	print(f"\t{topping}")

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'Haskell']
}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}.")




