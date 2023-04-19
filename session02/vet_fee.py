"""
A program accepts the number of hours (whole number) from the keyboard
and outputs the consultation fee to the screen.
"""

# CONSTANTS
HOURLY_RATE = 25

# input
hours = int(input("Enter the number of hours for your consultation: "))

# calculation
fee = hours * HOURLY_RATE

# output
print("Your fee is: $", fee)
