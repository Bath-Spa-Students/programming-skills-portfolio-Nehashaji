#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet.


my_pets = [
    {"kind": "Cat" , "owner": "Mary"},
    {"kind": "Fish" , "owner": "Steve"},
    {"kind": "Bird" , "owner": "John"},
    {"kind": "Hamster" , "owner": "Lily"},
]

for pet in my_pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}\n")