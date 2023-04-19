"""
This program will take in an exam score (0-100) and either output pass with a "Well done"
message when the score is above 50, else it will output fail with the message "Try again."
"""

# pseudocode
# Program pass_fail
#   INPUT score
#   IF (score > 50)
#       grade = Pass
#       message = "Well done"
#   ELSE
#       grade = Fail
#       message = "Try again"
#   ENDIF
#   OUTPUT grade, message
# END

# input
score = int(input("Enter your score out of 100: "))

#calculation
if score > 50:
    grade = "Pass"
    message = "Well done"
else:
    grade = "Fail"
    message = "Try again"

# output
print("Grade is {}, {}".format(grade, message))
