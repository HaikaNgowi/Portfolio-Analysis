current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

prompt = "\nTell me something, I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)

prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)	"
while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

