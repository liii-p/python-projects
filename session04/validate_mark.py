"""
This program will take input and validate an assessment mark (0-100)
and output Pass if the mark is 50 or above, otherwise output Fail.
"""
# input
mark = int(input("Enter your mark here (0-100): "))

while mark < 0 or mark > 100:
    print("Invalid mark.")
    mark = int(input("Enter your mark here (0-100): "))

if mark >= 50:
    print("Pass")
else:
    print("Fail")

