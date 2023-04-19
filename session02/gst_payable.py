"""
Program to calculate gst payable on item
"""

# input
item_cost = float(input("Enter the cost of your item: "))

# CONSTANTS
GST = 0.1

# calculation
gst_payable = item_cost * GST

# output
print("The GST payable is: ${:.2f}".format(gst_payable))

