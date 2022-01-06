#Cant get to run the codes for the input and while codes successfully pgs 112-117

message = input("Tell me something and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: Joy")
print(f"\nHello, {name}!")

prompt = "If yout tell us who you, we can personalize the message for you."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

height = input("How tall are you, in inches?  ")
height = int(height)

if height >= 48:
	print("\nYou are tll enough to ride.")
else:
	print("\nYou'll be able to ride when you are a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number is odd.")


