"""
This program will request the input of 5 numbers into a list and output
this to the console and write these to a text file.
"""

# bunch of pseudocode here

output_file = open("numbers.txt", "w")

scores = [None] * 5

for index in range(0, len(scores)):
    scores[index] = int(input("Enter your score:"))

print("Numbers in the list: ", len(scores))
print("The numbers are:")

for index in range(0, len(scores)):
    print(scores[index])

for index in range(0, len(scores)):
    output_file.write(str(scores[index]) + "\n")

output_file.close()

print("Scores in the list written to the file.")
