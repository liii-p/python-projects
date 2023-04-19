"""
This program will request the input of 4 numbers into a list and output this to the console.
"""


# Pseudocode
# scores[4]
#
# FOR index = 0 TO LENGTH(scores)
#   INPUT scores[index]
# ENDFOR
#
# OUTPUT HEADING
# FOR index = 0 TO LENGTH(scores)
#   OUTPUT scores[index]
# ENDFOR

def main():
    scores = [None] * 4
    total = 0
    average = 0

    for index in range(0, len(scores)):
        scores[index] = int(input("Enter your score: "))

    print(f"Numbers in this list: {len(scores):d}")

    for index in range(0, len(scores)):
        print(scores[index])

    for index in range(0, len(scores)):
        total = total + scores[index]

    average = total / len(scores)

    print(f"Total = {total:7d}")
    print(f"Average = {average:5.2f}")

#     Find the highest number in the scores List
    high = scores[0]

    for index in range(0, len(scores)):
        if scores[index] > high:
            high = scores[index]

    print(f"Highest value in the list = {high:d}")

main()
