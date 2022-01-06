cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchioves':
	print("\nHold the anchioves!")

#Numerical Comparisons
answer = 17
if answer != 42:
	print("\nThat is not the correct answer. Try again!")

#Multiple conditions
#Banned users
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"\n{user.title()}, you can post a response if you wish.")

#Boolean Expressions aka conditional statements

#Try It Yourself
#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

car != 'bmw'
print("\nIs car == 'bmw'? I predict False")
print(car != 'bmw')

car >= 'mazda'
print("\nIs car == 'bmw' I predict False")
print(car != 'mazda')
print(car == 'mazda')
print(car <= 'mazda')

car_1 = 'infinity'
car_0 = 'mitsubishi'
print("\nIs car_0 == 'mitsubishi' and car_1 == 'infinity'? I predict False")
print(car_0 != 'mitsubishi' and car_1 >= 'infinity')

