"""
    This program will output 'cold' when temp is below 20 or 'warm' otherwise
"""
# pseudocode
# Program temperature
#   INPUT temp
#   IF temp < 20 THEN
#       comment = 'cold'
#   ELSE
#       comment = 'warm'
#   ENDIF
#   OUTPUT comment
# END

# input
temp = int(input("Enter the temperature: "))

#calculation
if temp < 20:
    comment = "cold"
else:
    comment = "warm"

#  output
print("The weather is:", comment)

# print("The weather is: {}".format(comment))



