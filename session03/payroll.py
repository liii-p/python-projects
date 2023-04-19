"""
This program will allow a person to earn a base wage of $10k without paying tax,
otherwise they will pay a tax of 25% on the amount of $10k
"""

# Pseudocode
# Program payroll_calc
#      DEFINE CONSTANTS BASE=10000, TAX_RATE=0.25
#      INPUT gross_pay
#      IF gross_pay>BASE
#           tax=(gross_pay-BASE)*TAX_RATE
#      ELSE
#           tax=0
#      ENDIF
#      nett_pay=gross_pay-tax
#      OUTPUT nett_pay
# END

# CONSTANTS
BASE = 10000
TAX_RATE = 0.25

# input
gross_pay = int(input("Enter your gross pay: "))

if gross_pay > BASE:
    tax = (gross_pay - BASE) * TAX_RATE
else:
    tax = 0

nett_pay = gross_pay - tax
print("Your net pay is: ", nett_pay)


