# Variables and Data Types
# Operations and Expressions
# Conditionals - if else statements
# Loops - For Loop and While Loop
# Functions
# Lists 

# Write a python program which swaps 2 variables and then prints them

# x = 10
# y = 20

# x , y = y , x

# print(f"The value of the variable x is {x}")
# print(f"The value of the variable y is {y}")

# Take a user's name and print "Hello <user>"

# name = input("Enter name: ")
# print(f"Hello {name}")

# Calculate the area of a Circle given the radius.

# PI = 3.14
# radius = float(input("Enter Radius: "))
# area = PI * (radius ** 2)
# print(f"The Area of the Circle is {area}.")

# Write a program to check if a number is even or odd using the modulus operator.

# def even_or_odd(num):
#     if num % 2 == 0:
#         return "Even number"
#     else:
#         return "Odd number"

# # Main
# x = int(input("Enter a number: "))
# print(even_or_odd(x))

# RULES OF THUMB
# 1) Usually functiuons don't contain the input statement (You take input inside the main program)
# 2) A function will not work unless you call it inside the main program
# 3) A funtion can return a value ---- if it returns a value then you will need to use print statement in the main program to see the value it returned
# 4) If a funtion doesn't return a value - Then you can call the function directly (No need of a print statement)


# .append() .pop() .remove() .insert()

colors = ["green" , "blue" , "red"]

for color in colors:
    print(color)
