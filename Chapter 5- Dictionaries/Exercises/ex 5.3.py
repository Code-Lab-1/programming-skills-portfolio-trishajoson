#Now that you know how to loop through a dictionary, 
# clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms 
# to your glossary.When you run your program again, these new words and 
# meanings should automatically be included in the output.

glossary={
    "function" :"group of related statements that performs a specific task",
    "input": "Takes in an input from user.",
    "float":"represents a decimal number in python",
    "loops":"Used to iterate over a sequence",
}
for thing, key in glossary.items():
	print("{}: {}".format(thing, key))
 
 glossary.update({'int()': 'function returns an integer from a given object or converts a number in a given base to a decimal.','string':'Strings are text enclosed in single or double quotes.','variable':"A variable lets you store a value by assigning it to a name.",'=':'The equal sign is called the assignment operator and is used to assign a value to a variable.','comments':'Comments are annotations to code used to make it easier to understand. They don\'t affect how code is run.'})
 for thing, key in glossary.items():
	print("{}: {}".format(thing, key))