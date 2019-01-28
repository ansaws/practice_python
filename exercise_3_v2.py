#sucess
my_list = []

while True:
    my_list_len =len(my_list)
    append = None
    while append == None:
        try:
            append = input('Do you want to add a number to the list, press y for yes and press n no: ')
        except:
            print('Please input a y or n')
    if append == "y":
        while len(my_list) == my_list_len:
            try:
                my_list.append(int(input("Enter a number to input: ")))
            except:
                print("add a valid number to the list")
    if append == "n":
        break
    print("These are the items in your list so far: ")
    for item in my_list:
        print(item)
    

append_list = []
for item in my_list:
    if item<5:
        append_list.append(item)



if len(append_list)>0:
    print("These are the items in your list that are under 5:")
    for item in append_list:
        print(item)
if len(append_list)== 0:
    print("there are no items in your list")