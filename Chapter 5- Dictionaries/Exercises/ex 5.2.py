#Exercise 2: Glossary :ballot_box_with_check:

#A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.

#Print each word and its meaning as neatly formatted output. 

glossary={
    "function" :"group of related statements that performs a specific task",
    "input": "Takes in an input from user.",
    "float":"represents a decimal number in python",
    "loops":"Used to iterate over a sequence",
}

# You might print the word followed by a colon and then its meaning
print('function :', glossary['function'])
print('input:', glossary['input'])
print('float:',glossary["float"])
print("loop:",glossary["loops"])
