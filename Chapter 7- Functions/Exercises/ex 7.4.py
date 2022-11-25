# Exercise 4:  Large Shirts :ballot_box_with_check:
# Modify the make_shirt() function so that 
# shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

    
        
def make_shirt(size='large', txt_shirt='I love Python!'):
        print("The size of the shirt is",size,"and the message on it says '"+txt_shirt+"'")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Sky is blue.')