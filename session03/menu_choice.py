"""
This program will request the user for a menu choice 1, 2, 3 and executes that
choice (outputs a msg)
"""

# pseudocode
# program menu_choice
#   INPUT choice
#   CASE (choice)
#       1: result = "Your choice was 1"
#       2: result = "You picked choice 2"
#       3: result = "Alright, choice number 3 it is."
#       ELSE: OUTPUT "Invalid choice entered"
#   END CASE
#
#  OUTPUT result
# END

# input
choice = int(input("Enter your choice 1, 2, or 3: "))

# processing
menu = {1: "Your choice was 1",
        2: "You picked choice 2",
        3: "Alright, choice number 3 it is."}
result = menu.get(choice, "Invalid choice entered")

# output
print("Result: {}".format(result))

