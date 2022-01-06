# Lists [], index starts at 0, 
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-2].title())
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#Try It Yourself
#3.1 Names
names = ['Tosin', 'Faith', 'Alex', 'Chris', 'Grace','Belinda']
print(names[1].title())
message = f"My date, {names[3].title()}, has been so good to me lately."
print(message)

#3.2 Greetings
message = f"{names[-4].title()}, can you please lend me hand?"
print(message)

#3.3 My Own List
vehicles = ['BMW', 'Aston Martin', 'Bentley', 'Toyota', 'Lexus', 'Range']
message = f"My all time dream is to drive a {vehicles[2].title()}."
print(message)

#Modify elements in a list
vehicles[1] = 'Lamborghini'
print(vehicles)

#Add elements in a list - append adds at the end of the list
vehicles.append('Tesla')
print(vehicles)

#Inserting elements to a list adds elements anywhere in the list
vehicles.insert(1, 'Volvo')
print(vehicles)

#Removing elements from a list
#del - permanent
del vehicles[2]
print(vehicles)
#pop - remove last item, still workable in future
popped_vehicles = vehicles.pop()
print(popped_vehicles)
last_owned = vehicles.pop()
print(f"The last vehicle I owned was a {last_owned.title()}.")
#pop - remove items from any position in the list (add index)
first_owned = vehicles.pop(0)
print(f"The first vehicle I ever owned was a {first_owned.title()}.")
#remove() - used when position in the list is unknown
vehicles.remove('Volvo')
print(vehicles)
too_expensive = 'Bentley'
vehicles.remove(too_expensive)
print(vehicles)
print(f"\nA {too_expensive.title()} is too expensive to maintain.")

# Try It Yourself
#3.4 Guest List
Invitees = ['Faith', 'Tosin', 'Alex', 'Bettina', 'Grace', 'Belinda', 'Sanmi', 'Collin']
message = f"\n{Invitees[-2].title()}, you are cordially invited to the annual christmas dinner to be held at the Grand Melia Hotel."
print(message)

#3.5 Changing Guest List
non_attendee = 'Bettina'
message = f"\nUnfortunately, {non_attendee.title()} will not be able to join us for the annual dinner."
print(message)

#3.6 More Guests
Invitees.remove('Bettina')
Invitees.insert(3, 'Saraha')
Invitees.append('Miranda')
print(Invitees)
message = f"\nAs we all know {non_attendee.title()} will not make it to the dinner, please welcome {Invitees[3].title()} to our annual dinner."
print(message)
message = f"\nThank you for making the time to attend the annual dinner, we are pleased to welcome {Invitees[0].title()}, {Invitees[1].title()}, {Invitees[2].title()}, and {Invitees[5].title()}."
print(message)

#Sort lists - permanent, alphabetical order; sorted lists - temporary
vehicles = ['BMW', 'Aston Martin', 'Bentley', 'Toyota', 'Lexus', 'Range']
vehicles.sort()
vehicles.sort(reverse=True)
print(vehicles)
print("\nHere is the original list:")
print(vehicles)
print("\nHere is the sorted list:")
print(sorted(vehicles))
print("\nHere is the original list again:")
print(vehicles)

#reverse order of lists without sorting alphabetically (reverse)
vehicles.reverse()
print(vehicles)
vehicles.reverse()
print(vehicles)

# Lengths of lists
#Use terminal to identify length of lists (len())



