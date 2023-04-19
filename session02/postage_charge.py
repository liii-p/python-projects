"""
Calculate postage charge for parcel
"""

# pseudocode
# input
# parcel weight
# constant
# 1.5
# calculation
# parcel weight * const

#input
parcel_weight = float(input("Enter the weight of your parcel (kg): "))

#CONSTANTS
POSTAGE_RATE = 1.5

#calculation
parcel_cost = parcel_weight * POSTAGE_RATE

#output
print("The cost of your parcel is: ${:.2f}".format(parcel_cost))

