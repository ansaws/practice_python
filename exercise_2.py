#success
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently when divided by 2
'''

num = None

while num == None:
    try:
        num = int(input('Enter a whole number: '))
    except:
        print('Please input a valid value.')

if num%2 == 0:
    print(num, "is even")

if num%2 == 1:
    print(num, "is odd")