"""
This program will request the user for a number and a menu choice "a", "b" or "c"
and executes that choice ("a"- double the number, "b" - halve the number or "c" -
square the number).
"""

# Pseudocode
# Program calc_num
#   INPUT num1
#  INPUT choice
#  CASE (choice)
#       "a": result = num1 + num2
#       "b": result = num 1 / 2
#       "c": result = num ^ 2
#     ELSE: OUTPUT invalid choice - must be a, b or c
#  END CASE
#
#  OUTPUT result
# END

# input
num1 = int(input("Enter the number: "))
choice = input("Enter your choice, a - double the number, b - halve the number or c - square the number: ")

# processing
math = {"a": num1 + num1,
        "b": num1 / 2,
        "c": num1 ** 2}
result = math.get(choice, "invalid choice - must be a, b or c")

# output
print("The answer is {}".format(result))
