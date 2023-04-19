"""
This program will open a text file (addams.txt) and display the contents to the screen
"""


# Pseudocode
# Program input_addams_file_example
#   OPEN "addams.txt" FOR INPUT as input_file
#
#   FOR EACH line IN input_file
#       OUTPUT line
#   END FOR
#
#   CLOSE input_file
# END

def main():
    input_file = open("./TextDataFiles/addams.txt", "r")

    for line in input_file:
        print(line, end='')

    input_file.close()

    new_name = input("\nEnter your name:")
    output_file = open("./TextDataFiles/addams.txt", "a")
    output_file.write(new_name)
    output_file.write("\n")
    output_file.close()


main()
# Variable new name is out of scope here
# print(f"The new name is{new_name:s}")
