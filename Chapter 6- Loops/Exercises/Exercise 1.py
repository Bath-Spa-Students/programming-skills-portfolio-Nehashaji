#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

#print a message saying you’ll add that topping to their pizza.

toppings=[]

while True:
    #prompt for user to add toppings
    topping=input("Enter the pizza topping: (or type quit to quit the code)")

#if user type quit the code will break 
    if topping == 'quit':
        break

#add the topping to list "Toppings"
    toppings.append(topping)

print("This are your toppings:")
for i in toppings:
    print(i)