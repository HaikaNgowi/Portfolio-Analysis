# Tuples are immutable list of elements that use parentheses instead of square brackets and a comma
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
	print(dimension)

#4.13 Try It Yourself - why showing results four times?
Buffet = ('Salmon', 'Redsnapper', 'Greens', 'Shrimp')
for menu in Buffet:
	print(menu)

Buffet = ('Salmon', 'Crab', 'Greens', 'Lobster')
print("\nModified Menu:")
for menu in Buffet:
	print(menu[:])

    