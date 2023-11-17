# Exercise 4: Deli :ballot_box_with_check:
# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwhich_orders=['Francisco', 'Cheesy-creamy','Mega chicken','beef special']
finished_sandwhiches=[]

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print("Your " + current_sandwhich + " is being made.")
    finished_sandwhiches.append(current_sandwhich)

for sandwhich in finished_sandwhiches:
    print("I made" + sandwhich + " sandwhich.")