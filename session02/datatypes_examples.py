"""
Examples of python data types
"""

# datatype of variable is determined when first used

# input gives string type
# String (str)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print("Sum is: ", (num1+num2))
print("Data type of num1 is: ", type(num1))

# Numeric (int - whole numbers, float - numbers with decimal part)
# now we change to int
num1 = int(num1)
num2 = int(num2)
print("Sum is: ", (num1 + num2))
print("Data type of num1 is: ", type(num1))
# now we change to float
num1 = float(num1)
num2 = float(num2)
print("Sum is: ", (num1 + num2))
print("Data type of num1 is: ", type(num1))

# Boolean (bool - true/false)
old = num1 > 20
print("old is: {}".format(old))
print("Data type of old is: ", type(old))

# String
name = input("Enter your name: ")
print("Hello ", name)
# output the number of characters in your name
print("Your name has {} characters".format(len(name)))
