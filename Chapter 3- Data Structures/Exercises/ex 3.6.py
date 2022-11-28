#Exercise 6: Shrinking Guest List :ballot_box_with_check:

#You just found out that your new dinner table won’t arrive in time for the dinner, 
# and you have space for only two guests.
#Start with your program from Exercise 3-5. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them 
# know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them know they’re still invited.

#use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.


lprint("Sorry", list_guests[0],"I can't invite you to dinner.")
list_guests.pop(0)
print("Sorry", list_guests[0],"I can't invite you to dinner.")
list_guests.pop(0)
print("Sorry", list_guests[0],"I can't invite you to dinner.")
list_guests.pop(0)
print("Sorry", list_guests[0],"I can't invite you to dinner.")
del list_guests[0]
print("Sorry", list_guests[0],"I can't invite you to dinner.")
del list_guests[0]
print(list_guests)