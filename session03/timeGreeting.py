"""
This program uses datetime to determine the time and outputs
a greeting based upon the time of day/night.
"""
import datetime

# no inputs necessary for this program.
userTime = datetime.datetime.today().hour

# processing
if userTime < 12:
    message = "Good morning"
elif (userTime < 13) and (userTime > 12):
    message = "Lunch time"
elif userTime < 18:
    message = "Good afternoon"
else:
    message = "Good night"

# output
print(message)
