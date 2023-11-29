# f strings in Python
""" cat_name = "Boss"
cat_age = 5
animal_type = "cat" """
# print(f"{cat_name} is a {cat_age} year old {animal_type}")

# String functions (upper, lower, strip, capitalize, isdigit, islower,isupper, in )
""" my_cat = "winston"
print(my_cat.upper())
print(my_cat.capitalize())
my_other_cat = "MILLIE"
print(my_other_cat.lower().capitalize())
print(my_other_cat)
print(my_other_cat.center(30,"*"))

num = "5"
character = "^"
print(num.isdigit())
print(character.isalpha())
print("Sto check")
does_contain = "Mill" in my_other_cat
print(does_contain) """

# Accessing single characters within a string
###  M   i   L   L   i   e  ####
###  0   1   2   3   4   5  ####
### -6  -5  -4  -3  -2  -1 #### 

""" cat_name = "WiNStON"
length = len(cat_name)
print(cat_name[length-2])
print(cat_name[-4]) #should be S
print(cat_name[5]) #should be O

# Number of occurences of a character in a string
my_cat_name = "MiLLie"
print(my_cat_name.count("L"))

#Example: number of spaces in a string
my_sentence = "The quick brown fox jumps over the lazy dog"
num_spaces = my_sentence.count(" ")
print(num_spaces)
 """




# Accessing multiple characters in a string(slicing)
# syntax possiblities:
# string[start:stop], string[start:], string[:stop]
# string[:], string[start:stop:step], string[::step]
# up to but not including the last index


### T  h  i  s   i  s   a   s  t  r  i  n  g ###
### 0  1  2  3 4 5  6 7 8 9 10 11 12 13 14 15

string_one = "This is a string"

# string[start:stop], string[start:], string[:stop]

# my_substring = string_one[:8]
# print(my_substring)
# my_substring = string_one[8:]
# print(my_substring)
# my_substring = string_one[4:12]





### T  h  i  s   i  s   a   s  t  r  i  n  g ###
### 0  1  2  3 4 5  6 7 8 9 10 11 12 13 14 15

# string[:], string[start:stop:step], string[::step]
my_substring = string_one[:]
print(my_substring)
my_substring = string_one[1:10:2]
print(my_substring)
my_substring = string_one[::4]
print(my_substring)
my_substring = string_one[1::3]
print(my_substring)
my_substring = string_one[:14:2]
print(my_substring)
#negative indices
my_substring = string_one[-1:-6:-2]
print(my_substring)

#reverse string
my_substring = string_one[::-1]
print(my_substring)
#rearranging strings with slicing
not_yoda_sentence = "I will take you to him"
#yoda_sentence should be Take you to him, I will

#### I   w i l l   t a k e     y  o  u     t  o      h  i  m ####
#    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18  19 20 21

first_part = not_yoda_sentence[7:].capitalize()
second_part = not_yoda_sentence[0:6]
yoda_sentence = f"{first_part}, {second_part}"
print(yoda_sentence)