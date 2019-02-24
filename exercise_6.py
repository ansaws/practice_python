#sucess
string = None
while string == None:
    try:
        string = input("enter a string: ")
    except:
        print("please enter a valid value")

list_string = list(string)
if list_string == list(reversed(list_string)):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")