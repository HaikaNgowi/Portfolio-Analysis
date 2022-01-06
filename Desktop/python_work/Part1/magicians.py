# A for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	print(f"{magician.title()}, that was a great trick!")
	print(f"I cant wait to see your next trick, {magician.title()}\n")
print("Thank you everyone. That was a great show!\n")

# Range of numbers (n-1)
for value in range(1, 6):
	print(value)
for value in range(6):
	print(value)

#Range to create lists of numbers
numbers = list(range(1, 6))
print(numbers)

#print even numbers between 1 and 10
even_numbers = list(range(2,11,2))
print(even_numbers)

#squares - first 10 square numbers
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
	print(squares)

square = []
for value in range(1,11):
	square = value ** 2
	print(square)

squares = []
for value in range(1,11):
	squares.append(value**2)
	print(squares)

#list comprension of the above
squares = [value**2 for value in range(1,11)]
print(squares)

odd_number = []
for value in range(1,21):
	odd_number = list(range(1,21,3))
	print(odd_number)