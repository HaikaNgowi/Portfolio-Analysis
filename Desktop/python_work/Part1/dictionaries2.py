#Dictionary of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
#keys
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
	print(name.title())
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi, {name.title()}")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"Hi {name.title()}, I see you love {language}!")
	if 'erin' not in favorite_languages.keys():
		print("Erin, please take our poll!")
for name in sorted(favorite_languages.keys()):
	print(f"\n{name.title()}, Thank you for taking the poll!")

#Values
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())


# Use get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
point_value = alien_0.get('points')
print(point_value)

#Try it yourself
interviewee_info = {
	'first_name': 'Kris',
	'last_name': 'Curtis',
	'age': '35',
	'city': 'Washington',
	'time': 'EST',
}

print(f"{interviewee_info['first_name'].title()}, your interview is scheduled in {interviewee_info['city'].title()} at 10 am {interviewee_info['time'].upper()}.")


