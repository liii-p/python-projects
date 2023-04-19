"""
This program will initialise a list of 4 numbers and output to the console
"""


# Pseudocode
# scores[4]
#
# scores[0] = 2
# scores[1] = 1
# scores[2] = 10
# scores[3] = 9
#
# OUTPUT HEADING
# FOR index = 0 TO LENGTH(scores)
#   OUTPUT scores[index]
# ENDFOR

def main():
    scores = [None] * 4

    scores[0] = 2
    scores[1] = 1
    scores[2] = 10
    scores[3] = 9

    #     scores = [2, 1, 10, 9]
    # or you can assign values collectively, comment out the above 5 lines

    print(f"Numbers in list: {len(scores):d}")
    for index in range(0, len(scores)):
        print(scores[index])


main()
