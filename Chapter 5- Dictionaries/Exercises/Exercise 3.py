#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
"Function": "Piece of prewritten code that performs an operation.",
"Variable": "Name that represents a value stored in thecomputer memory ",
"String":"Sequence of characters that is used as data.",
"List":"An object that contains multiple data items.",
"Boolen expression":"Expression tested by if statement to determine if it is true or false.",
"Set": "object that stores a collection of data in same way  as mathematical set",
"Sentinel" : "special value that marks the end of a squence of items.",
"Logical operators": "operators that can be used to create complex Boolean expressions.",
"Dictionary": "object that stores a collection of data.",
"len function": "used to obtain number of elements in a  dictionary"
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")


