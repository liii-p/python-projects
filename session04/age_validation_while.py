"""
This program will validate an age entered by the user and calculate days old...
"""
# Pseudocode
# Program age_validation_while
#   INPUT age
#   WHILE (age < 0 OR age > 130)
#       OUTPUT error
#       INPUT age
#   ENDWHILE
#   OUTPUT age * 365
# END

age = int(input("Enter age between 0 and 130: "))

while not (age >= 0 and age <= 130):
# while age < 0 or age > 130:
    print("Erorr - age out of range")
    age = int(input("Enter age between 0 and 130: "))

age_in_days = age * 365
print("Age in days = ", age_in_days)

