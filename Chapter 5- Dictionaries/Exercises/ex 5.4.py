## Exercise 4: Rivers :ballot_box_with_check:
# Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers={
    'Nile':'Egypt',
    'Chang Jiang':'China',
    'Irtish':'Russia',
    'Yukon':'Canada'
    }

for river, country in rivers.items():
	print("{} runs through {}".format(river, country))
 
for river in rivers.keys():
	print(river)

for country in rivers.values():
	print(country)