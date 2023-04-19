"""
This program will determine whether a string contains all numbers
and outputs "correct", otherwise it outputs "incorrect"
"""

# inputs
idString = input("Enter your student ID, it must be entirely numerical: ")

# processing
numericCheck = idString.isnumeric()

# output
if not numericCheck:
    print("Your ID is incorrect.")
else:
    print("Your ID is correct.")
