# Unit 6 Lesson 4 - List Methods

import random

# count - returns the number of occurences
# of some character

my_list = [1,2,3,1,2,'a','b']
num_twos = my_list.count(2)
num_as = my_list.count('a')
#print(num_twos)
#print(num_as)

# append
my_list.append('c')
#print(my_list)
last_item = my_list.pop()
#print(last_item)
#print(my_list)
my_list.append(['c','d'])
#print(my_list)
my_list.pop()
# extend - adds the items in a 
# list/tuple to the end of a list
my_list.extend('c')
#print(my_list)

# .sort() vs sorted()
num_list = []
for i in range(20):
    num_list.append(random.randint(1,100))
#print(num_list)
#print(num_list.sort())
#print(num_list) # original num_list no longer exists
                # since lists are mutable
#sorted_list = num_list.sort()
#print(sorted_list)
# sorted_list = sorted(num_list)
# sorted_list.reverse()
# print(num_list)
# print(sorted_list)
my_animals= ['Aardvark','Camel','Bear','Rhino']
# ascii values are [97,65,98,36,123,40]
#print(sorted(my_animals))

my_nums = [1,2,3,4,5]
my_nums.pop()
#print(my_nums)
val = my_nums.pop(1)
#print(my_nums)
#print(val)

final_list = []
for i in range(20):
    final_list.append(random.randint(1,100))

# remove 20

try:   
    location = final_list.index(20)
    final_list.pop(location)
    print(f"Item removed from index {location}")
except ValueError:
    print("Number not found")



