#sucess
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
 Make sure your program works on two lists of different sizes.
"""
import random
index = 0
list_1 = []
list_2 = []
common_list = []
common_list_1 = []
for num in range(1,10):
    list_1.append(random.randint(1,11))
    list_2.append(random.randint(1,11))

print(list_1 )
print(list_2)
common = False

while index<9:
    for num in list_2:
        if common == False: 
            if num == list_1[index]:
                common_list.append(num)
                common = True
    common = False
    index+=1
index = 0
while index<len(common_list)-1:
    for num in common_list:
        if common == False: 
            if num == common_list[index]:
                common = True
                common_list.remove(num)
    common = False
    index+=1
print("these are the common values:")
print(common_list)
