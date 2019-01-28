#success
'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


num_int_type = None
num_1 = num
if num%2 == 0:
    num_1 = num/2
    num_1 = int(num_1)

if num%2 == 1:
    num_int_type = "odd"

if num_int_type == "odd":
    num += 1
    num_1 = num/2
    num_1 = int(num_1)
    num -=1



'''

num = None

while num == None:
    try:
        num = int(input('Enter a whole number: '))
    except:
        print('Please input a valid value.')


dividends = range(1,num + 1 )
divisors = []

for dividend in dividends:
    if num%dividend == 0:
        divisors.append(dividend)

print("Here are the divsors of", num)

for number in divisors:
    print(number)

