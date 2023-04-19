"""
This program takes a student ID input from user and identifies whether it is alphanumeric
in which case it outputs "correct", else "incorrect"
"""

# input
userID = input("Enter your student ID, it must be entirely alphanumeric: ")

# processing
isLettersID = userID.isalpha()

# output
if not isLettersID:
    print("Your ID is incorrect")
else:
    print("Your ID is correct")
