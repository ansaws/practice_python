#success

'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

def add_age(input_age, years_added):
    age = int(input(input_age))
    age += years_added
    print("Your age in", years_added, "years will be", age,".")






try:
    add_age("What is your age:", 100)
except:
    print("Please enter a valid value")
    add_age("What is your age:", 100)
