"""
This program will input a series of numbers (enter 0 to end)
and find the largest and smallest of the numbers entered.
"""
# Pseudocode
# Program series_of_numbers
#   WHILE user doesn't enter 0
#       INPUT nums
#      IF num == 0
#       find smallest num
#       find biggest num
#       OUTPUT smallest and biggest num
#   ENDWHILE
# END

arr = []

while True:
    num = int(input("Enter a number (Enter 0 to exit): "))
    arr.append(num)
    if num == 0:
        arr.remove(0)
        lrgNum = max(arr)
        smlNum = min(arr)
        print("The largest num is {} and the smallest is {}".format(lrgNum, smlNum))
        break
