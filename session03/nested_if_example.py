"""
This program will request the user for a temp and outputs "freezing" when it is below 0
"mild" when it is below 30, "hot" when below 40, otherwise "boiling!
Too hot to do anything"
"""

# pseudocode
# Program nested_if_example
#   INPUT temp
#   IF temp < 0
#       comment = "freezing"
#   ELSE
#       IF temp < 40
#           comment = "hot"
#       ELSE
#           comment = "boiling! Too hot to do anything"
#       ENDIF
#     ENDIF
# ENDIF
# OUTPUT comment
# END

# input the temp
temp = int(input("Enter the temperature: "))

# determine the comment
if temp < 0:
    comment = "freezing"
elif temp < 30:
    comment = "mild"
elif temp < 40:
    comment = "hot"
else:
    comment = "boiling! Too hot to do anything."

# output
print("The weather is {}".format(comment))
