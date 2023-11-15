#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders= ['Chicken' , 'Pastrami' , 'Cheese', 'Club', 'Pastrami', 'Beef' , 'Zinger' , 'Pastrami' ]

print("Sorry, We run out of pastrami .")

while 'pastrami' in sandwich_orders: 
    sandwich_orders.remove('pastrami')

while 'pastrami' in sandwich_orders:
   current_order = sandwich_orders.pop(0)
   print(f"I made your {current_order} sandwich.")
   finished_sandwiches.append(current_order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)