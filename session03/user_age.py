"""
This program will accept user's age and then output "You are a child" if under 18
otherwise "You are an adult"
"""
# input
age = int(input("Enter your age: "))

# processing
if age < 3:
    print("You are a toddler")
elif age < 18:
    print("You are a child.")
elif age <= 40:
    print("You are an adult.")
elif age <= 65:
    print("You are middle-aged.")
else:
    print("You are over the hill!")



