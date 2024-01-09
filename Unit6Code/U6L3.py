# Unit 6 Lesson 3

# reversing using tuples

a = 10
b = 15

(a,b) = (b,a)

# print(f"a = {a}, b = {b}")

# assigning multiple values at once

c,d = 15,20

# print(f"c = {c}, d = {d}")

# enumeration

# nfc_north = ['Lions', 'Vikings', 'Packers', 'Bears']
# for index,team in enumerate(nfc_north):
#     print(f"Team# {index+1}: {team}")

my_list = [1,2,(3,4)]
print(my_list)
# valid
my_list[1] = -2
my_list[2] = (-3,-4)
print(my_list)
# invalid
# my_list[2][0] = 3
# print(my_list)
my_tuple = (1,2,[3,4])

# invalid
# my_tuple[0] = -1
# my_tuple[2] = [-3,-4]
my_tuple[2][0] = -3
my_tuple[2][1] = -4
print(my_tuple)

# CodeHS

#8.3.6
#8.3.8
#8.3.9