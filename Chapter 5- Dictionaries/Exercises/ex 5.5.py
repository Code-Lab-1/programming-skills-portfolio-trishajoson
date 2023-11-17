# Exercise 5: Pets :ballot_box_with_check:
# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet

pets=[]
Blackie = {
	'animal': 'dog',
	'owner': 'Trisha',
}
pets.append(Blackie)
Bombom = {
	'animal': 'hamster',
	'owner': 'Riya',
}
pets.append(Bombom)
Tom = {
	'animal': 'cat',
	'owner': 'Joson',
}
pets.append(Tom)

for pet in pets:
    print("{}".format(pet))