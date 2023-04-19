"""
Determine the discount on an item
"""

# INPUTS
# item price
# CONST
# Discount rate
# CALCULATION
# price times discount rate
# OUTPUT
# Discount

#assign constants
DISC_RATE = 0.1

#input
price = float(input("Enter the price of the item: "))
# price can be entered as decimal value

#processing
discount = price * DISC_RATE

# output
# print("The discount is $", discount)

# ouput formatted with 2 decimal places
print("The discount is $ {a:.2f}".format(a=discount))

# output discounted price
print("The discounted price is $ {a:.2f}".format(a=(price-discount)))
