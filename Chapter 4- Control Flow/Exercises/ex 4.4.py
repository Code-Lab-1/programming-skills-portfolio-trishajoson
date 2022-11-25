## Exercise 4: Stages of Life :ballot_box_with_check:
# Write an if-elif-else chain that determines a person’s stage of life. 
# Set a value for the variable age, and then:
# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

age= 70

if age<2:
    print("Person is a baby")
elif age>=2 and age<4:
    print("Person is a toddler")
elif age>=4 and age<13:
    print("Person is a kid")
elif age>=13 and age<20:
    print("Person is teenager")
elif age>20 and age<65:
    print("Person is an adult.")
else:
    print("Person is an elder")