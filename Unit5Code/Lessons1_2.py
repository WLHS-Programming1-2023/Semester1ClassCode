# f strings in Python
# animal_type = "cat"
# animal_name = "Winston"
# animal_age_years = 0.4

# print(f"My {animal_type} is name {animal_name} \
# and he is {animal_age_years} years old.")
# String functions (upper, lower, strip, capitalize )

# print(animal_name.upper())
# print("Millie".lower())
# print("millie".capitalize())
# print("My other cat is named Millie".capitalize())
# print("&M".capitalize())
# print("            Millie          ".strip())
# print(animal_name.center(11,"*"))
# character = "H"


# Number of occurences of a character in a string
# substring = "An"
# string = "Banana"
# print(substring in string)
# count = string.count(substring.lower())
# print(f"In the string {string} the substring {substring.lower()}\
#  shows up {count} times.")

# other_cat = "    MiLLie                 "
# print(other_cat.strip().capitalize().center(40,"$"))

###

# Accessing single characters within a string
###  M  i  L  L  i  e  ####
###  0  1  2  3  4  5  ####
### -6 -5 -4 -3 -2 -1  #### 

cat_name = "MiLLie"
print(cat_name[1])
print(cat_name[-5])
#print(cat_name[6]) # out of bounds error
length = len(cat_name) # length of string which is 6
print(cat_name[length-1])
print(cat_name[2])


# Accessing multiple characters in a string(slicing)
# syntax possiblities:
# string[start:stop], string[start:], string[:stop]
# string[:], string[start:stop:step], string[::step]
# up to but not including the last index

my_string = "This is a string"
### T  h  i  s   i s   a   s  t  r  i  n  g ###
### 0  1  2  3 4 5 6 7 8 9 10 11 12 13 14 15

# string[start:stop], string[start:], string[:stop]
word_this = my_string[0:4]
print(word_this)
print(my_string[:4])
word_string = my_string[10:]
print(word_string)

my_string.find(" ")


### T  h  i  s   i  s   a   s  t  r  i  n  g ###
### 0  1  2  3 4 5  6 7 8 9 10 11 12 13 14 15

# string[:], string[start:stop:step], string[::step]
word_step = my_string[16:10:-1]
print(word_step)


#backward string
reverse_string = my_string[::-1]
print(reverse_string)
