# Exercise 5: No Pastrami :ballot_box_with_check:
# Using the list sandwich_orders from Exercise 7-8, 
# make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwhich_orders=['Francisco', 'Cheesy-creamy','pastrami','Mega chicken','pastrami',
                  'beef special','pastrami']
finished_sandwhiches=[]

print("The pastrami has ran out sorry.")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')


while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print("Your " + current_sandwhich + " is being made.")
    finished_sandwhiches.append(current_sandwhich)

for sandwhich in finished_sandwhiches:
    print("I made" + sandwhich + " sandwhich.")