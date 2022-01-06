#Block of code designed to perform a single task stored in modules
def greet_user():
    """ Display a simple greeting."""
    print("Hello!")
greet_user()

def greet_user(username):
    """ Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')

#username is a parameter; useful for a function definition to work; jesse an example of an argument - info passed from a function call to another
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

##Multiple function calls
#add a describe pet for the additional call
describe_pet('dog', 'willie')

#Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

#Equivalent function calls
#A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
#Function with a while loop - run on terminal
def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted."""
    full_name = f"{first_name}  {last_name}"
    return full_name.title()
##This is an infinite loop
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# After first print enter the folloing for the infinite loop
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
        l_name = input("Last name: ")
        if l_name == 'q':
            break
        formatted_name = get_formatted_name(f_name, l_name)
        print(f"\nHello, {formatted_name}!")
























