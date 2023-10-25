#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.  


guests = ['Emma', 'Miko', 'Willam']

name = guests[0].title()
print(name + ", I would like you to join for dinner.")

name = guests[1].title()
print(name + ", I would like you to join for dinner.")

name = guests[2].title()
print(name + ", I would like you to join for dinner.")

print("As per the restaurant, there is space for only two guests ")
#Remove guests from the list using pop() until only two names remains
for _ in range(len(guests)-2):
    removed_guest = guests.pop()
    print(f"Sorry , {removed_guest}, I cant invite you to dinner.")

#Print a message to the two prople still on your list.
for guest in guests :
    print(f"{guest},you're still invited to dinner .")

#Use del to remove the last two names from your list.
del guests[:]

#print your list to make sure it's empty 
print ("Guest list:" , guests)