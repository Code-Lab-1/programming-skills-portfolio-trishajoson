#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. 
# You’ll have to think ofsomeone else to invite.

#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

#Modify your list, replacing the name of the guest who can’t make it 
# with the name of the new person you are inviting.

#Print a second set of invitation messages, one for each person who is still in y

list_guests= ['Riya', 'Mimi', 'Sharvari','Ash','John']
print("Unfortunately"+ list_guests[4],"cannot make it to dinner.")
del(list_guests[4])
list_guests.insert[]