# Unit 6 Lesson 4 - List Methods

import random

# count - returns number of times something appears
my_list = [1,2,3,1,2,'a','b']
num_twos = my_list.count(2)
count_a = my_list.count('a')
#print(num_twos)
#print(count_a)

# append
my_list.append('c')
#print(my_list)
#print(my_list.append('d')) # will not print list, prints None
#print(my_list)

# pop - removes and returns last item from a list 
my_list.pop()
#print(my_list)
for i in range(3):
    my_list.pop()
#print(my_list)

# more appending
my_list.append(['a','b','c'])
#print(my_list)

#extend - adds list of items to the end of a list
my_list.pop()
my_list.extend(['a','b','c'])
#print(my_list)

# .sort() vs sorted(list)
num_list = []
for i in range(20):
    num_list.append(random.randint(1,100))

print(num_list)
sorted_list = num_list.sort()
print(sorted_list)
print(num_list)
# issue with .sort() is that it permanently
# changes the list in memory - cannot go back
# because lists are mutable
print(""*5)
num_list2 = []
for i in range(20):
    num_list2.append(random.randint(1,100))
sorted_list2 = sorted(num_list2)
print(num_list2)
print(sorted_list2)

print("\n"*3)
my_chars = ['a','A','b','$','{','(']
# [97,65,98,36,123,40] are the ASCII values
# and it sorts their ASCII values then
# converts back
print(sorted(my_chars))

my_nums = [1,2,3,4,5]
my_nums.reverse()
print(my_nums)
my_nums.remove(5)
print(my_nums)


