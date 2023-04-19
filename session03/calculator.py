"""
This program will be a simplified calculator
"""

# input
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
op = input("Enter an operator +, -, *, /: ")

# processing
calc = {"+": num1 + num2,
       "-": num1 - num2,
       "*": num1 * num2,
       "/": num1 / num2}
result = calc.get(op, "Invalid choice, must be + - * /")

# output
print("{} {} {} = {}".format(num1, op, num2, result))


