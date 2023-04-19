
# creates an empty list
name_list = []

# loop while name is not ""

name = input("Enter a name: ")

while name != "":
    name_list.append(name)
    name = input("Enter another name (or <enter> to finish): ")

for the_name in name_list:
    print(the_name)

# open file for writing
output_file = open("my_names.txt", "w")

# write the names to the text file
for the_name in name_list:
    output_file.write(the_name + "\n")

# close the text file
output_file.close()