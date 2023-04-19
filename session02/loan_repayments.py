"""
calculate monthly repayments on customer loan
"""

# input
p = float(input("Enter your principal amount: "))
t = float(input("Enter the length of the loan (years): "))
r = float(input("Enter the annual interest rate: "))

# calculation
print("Calculating...")

result = p*((1+r*t)/100.0)/(12*t)

print("Inputs: P =", p, " T =", t, " R =", r, " M =", result)
