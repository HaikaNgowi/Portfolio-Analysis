#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:04:41 2021

@author: ikah
"""

# Moving items from one list to another:
# Start with users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

#Display all confirmed users
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title()) 

#Removing all instances of specific values from a list
#remove(): for one appearance of a value; while loop for several appearances
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
#with indent the results appear till all cats are removed; without indent only the final results
	print(pets)
print(pets)

#Filling a dictionary with user input
responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	#Prompt for the persons name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb? everest")
	#Store response in the dictionary
	response[name] = response
	#Find out of anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes/ no) yes")
	if repeat == 'no':
		polling_active = False
#Polling is complete show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")




