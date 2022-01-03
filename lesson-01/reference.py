# Print Hello World!
print("Hello World!") # The "" are essential, try without them!

# Making a string variable
name = "Sensei Ro"
print(name) 

# Learn more about variable names here: https://www.w3schools.com/python/gloss_python_variable_names.asp

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

"""

# Adding Strings together:
# You can add two or more strings together like so:
print("hello " + "world")

# Make a variable called greeting that says hello before the name variable, and then print it
greeting = "Hello " + name
print(greeting)

# Setting a string variable to input:
your_name = input()
print("Hello " + your_name)

# Take in number input 
# Creating number variables
# create two variables, with one variable being set to 1, and the other to 2.2
my_num = 1
my_other_number = 2.2

# Operations 
# + - * / add, subtract, multiply and divide two numbers respectively 

# Example:
a = 1
b = 2
print(a + b)

c = a + b
print(c) # Does the same thing

# Make variables d and e, d is equal to 5, e is equal to 10
# print d - e without making a new variable

d = 5
e = 10
print(d - e)

# Make variables my_num and my_other_num, set these variables to whatever number you want
# Make a variable called quotient that is equal to my_num times my_other_num
# print quotient - 1
my_num = 10
my_other_num = 12
quotient = my_num * my_other_num
print(quotient - 1)

# Adding strings and numbers
print(3 + "4") # Doesn't work because these two values are of different types
print("Your number is " + 3) # Also doesn't work

# Convert from strings to numbers
# use int() to convert a string to an integer (a number without a decimal)
string_number = "4"
print(3 + int(string_number))

# use float() if your number has a decimal value
string_decimal = "3.1"
print(1.1 + float(string_decimal))

# By default, input() returns you a string value
print(1 + input()) # will give you an error
print(1 + int(input())) # Works

# What does this code do?
your_number = int(input())
print("Your number + 1 is " + str(your_number + 1))

# Boolean values:
# Boolean values are really simple, they're either True or False
my_bool = True
my_false_bool = False

# Logical Operators
# You can use "Logical Operators" to return simple logic
# The logical operators are and, or, not
my_truth_value = True or False 
print(my_truth_value)

is_false = (True or False) and False
print(is_false)

# What does this print?
a = True
b = False
print((a or b) and (not a and not b))

# Conditional Operators:
# These operators return true or false based on certain conditions
""" They are
> (greater than)
== (equal to)
< (less than)
<= (less than equal to)
>= (greater than equal to)
!= (not equal to)
"""

a = 1
b = 2
print(a > b) # Prints False because 1 is not greater than 2

# Make three variables and compare then with at least 4 different conditional operators and 2 different logical operators
# At least one should print true and one should print false

# Kids can do whatever here
