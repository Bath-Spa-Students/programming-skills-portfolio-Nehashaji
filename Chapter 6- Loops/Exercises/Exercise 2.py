#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket.

var = "Your age"
var += "\n Enter 'quit' when you'r finished. "

while True:
    age = input(var)
    if age== 'quit':
        break
    age = int(age)

    if age < 3:
        print("Free entry")
    elif age <12:
        print("Ticket charge $10 ")
    else: 
        print("Ticket charge $15")
