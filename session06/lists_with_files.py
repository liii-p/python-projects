"""
This program will open a text (adams.txt) and read the contents to a list and display
the list to the screen
"""


# bunch of pseudocode here

def main():
    list_data = []

    input_file = open("adams.txt", "r")

    for line in input_file:
        list_data.append(line)

    input_file.close()

    for the_name in list_data:
        print(the_name, end="")

    print("\n")
    print(f"Names in the list: {len(list_data):d}")


main()
