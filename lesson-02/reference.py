# String review
# Add two strings
my_string = "Hello "
my_other_string = "World"
my_final_string = my_string + my_other_string

# Input review
# Add input to string
my_string = "Hello "
my_other_string = input()
my_final_string = my_string + my_other_string

# Warm up:

# Input 3 numbers, label them a, b 
# print the sum or a and b

# If statement
if True:
    print(True)
else:
    print(False)


# boolean reivew
my_bool = (a >= a) # my_bool = a >= a is valid too, but I prefer using parentheticals

# if statements
if my_bool:
    print(True)
a = 1
b = 2
if a >= b:
    print(True)
else:
    print(False)

# Questions:
# Take in 2 numbers, print out the greater number
# Numbers will not equal each other

a = int(input())
b = int(input())
if a > b:
  print(a)
else:
  print(b)

# Take in 2 numbers, print out the smallest number
# If one of the numbers is 0 print bazinga!
# One way of doing it:
a = int(input())
b = int(input())
if a == 0 or b == 0:
  print("bazinga!")
if a < b:
  print(a)
elif b < a:
  print(b)

# Take in 2 numbers, print "yes" if the difference of first and second number is 2 and "no" if that is not the case
a = int(input())
b = int(input())
if a - b == 2:
  print("yes")
else:
  print("no")

# Take in two numbers. If a is greater than b print "greater", if equal print "equal" or print print less
a = int(input())
b = int(input())
if a > b:
    print("greater")
elif a == b:
    print("equal")
else:
    print("lesser")

# find the issue with this code
# number = 101
# if number > 50:
#     print("number is greater than 50 but not greater than 100")
# elif number > 100:
#     print("number is greater than 100")
# else:
#     print("number is not greater than 50 or 100")

# It will never print the number is greater than 100 if it is

# For loops
# for i in range(100):
#     print(i)


# NOTE: i is a VARIABLE, but don't change it inside your loop. That's bad news
# for i in range(100):
#   a = i + 1
#   print(i)

# Example:
# Print a 10, but with x amount of zeros
# i.e. print 10 but with 3 zeroes
output = 1
power = int(input())
for i in range(power):
  output *= 10
print(output)

# You can also do this
output = 1
power = int(input())
for i in range(power):
  output *= 10
print(output)

# an alternate and valid way of doing this is with math functions we'll cover later
# feel free to google it tho

# Now make a string called dan
# you will take a number
# print dan that many times in one line with spaces
output = ""
for i in range(int(input)):
  output += " dan"
print(output)

# REVIEWS
# print the remainder of x /2 (x can be any number)

# take 1 number as input
# if the number is divisible by 2, print even
# if the number is not divisible by 2, print odd 

a = int(input())
if (a % 2 == 0):
    print("even")
else:
    print("odd")
