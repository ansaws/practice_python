#sucess
"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right."""
from random import randint
num = randint(1,10)
u_input = None
guess = 0
while True:
    while guess == 0:
        try:
            u_input = int(input("Gues the lucky number(hint: its between 1- 9): "))
            if u_input>0 and u_input<10:
                guess+= 1
            else:
                print("please iput a valid answer")
        except:
            print("please input a valid answer")
    if u_input>num:
        print("your number was too high please try again")
    elif u_input<num:
        print("your number was too low please try again")
    elif u_input == num:
        print("CORRECT!!!!!!!")
        break
    guess = 0
