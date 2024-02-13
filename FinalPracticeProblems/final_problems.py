#Write the code that tells someone that the value of PI is constant and equal to 3.14159.

PI = 3.14159

#Write an if statement that prints out “WooHoo!” if donutCount is greater than 10 and price is equal to zero (assume both donutCount and price are integers)

donutCount = 20
price = 0

if donutCount > 10 and price == 0:
    print("WooHoo!")

#Write a for loop that prints out the contents of a list, one element per line
    
my_list = [1,2,3,4]

for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])

#Write a function that takes parameters int_one and int_two and returns the square root of their product
import math

def sqrt_product(int_one, int_two):
    product = int_one*int_two
    return math.sqrt(product)

# Prompt a user to enter a number between 90 and 100. If they 
# enter a number out of bounds, tell them and prompt them again

while True:
    try:
        user_num = int(input("Enter a number between 90 and 100: "))
        if user_num >= 90 and user_num <= 100:
            print("Good choice")
            break
        else:
            print("Out of bounds")
    except ValueError:
        print("Not a number")

#Write a function that takes no parameters and prints a string that tells how to
#find the area and circumference of a circle (Something like A = PI * … and C =
#2 * ….)
        
def circle_formulas():
    print("The area of a circle is A = pi*r*r and the circumference is C = 2*pi*r")

circle_formulas()

#Write a function that uses an f string to tell the user if a given string parameter is a palindrome in the following format, supposing the word is “headphones”
# “Sorry, the word headphones is not a palindrome”
#If the word is “racecar”
#“Congrats, the word racecar is a palindrome!”

def palindrome_checker(word):
    if word == word[::-1]:
        print(f"Congrats, the word {word} is a palindrome!")
    else:
        print(f"Sorry, the word {word} is not a palindrome")

palindrome_checker("levels")
#Write a function that takes in a string and prints each word on a line, not including the spaces.

def word_printer(user_string):
    word_list = user_string.split()
    for word in word_list:
        print(word)
