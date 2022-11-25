# Exercise 3: T-Shirt  :ballot_box_with_check:
# Write a function called make_shirt() that accepts a size and the text of a message 
# that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.


def make_shirt(size,txt_shirt):
    
    print("The size of the shirt is",size,"and the message on it says '"+txt_shirt+"'")
    
make_shirt("M","I love coding.")

make_shirt(size="XL", txt_shirt="Stranger Things")