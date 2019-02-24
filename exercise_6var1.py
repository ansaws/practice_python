#sucess
"""
Ask the user for a string and print out whether this string is a palindrome or not. A palindrome is a string that reads the same forwards and backwards.
"""
move_on = None
list_1 = []
while True:
    len_list = len(list_1)
    while len(list_1) == len_list:
        try:
            list_1.append(int(input("Please input a number: ")))
        except:
            print("please input a valid value")
    while move_on == None:
        try:
            move_on = int(input("Do you want input more values into the list press 0 for yes and 1 for no"))
        except:
            print("please input a valid answer")
        if move_on == 0 or move_on == 1:
            pass
        else:
            move_on = None
            print("please input a valid answer")
    if move_on == 1:
        break
    move_on = None
if list_1 == list(reversed(list_1)):
    print("This list", list_1," is a palindrome")
else:
    print("This list", list_1," is not a palindrome")