# INPUT
# user's chosen letter
# OUTPUT
# ASCII equivalent of said letter

# user may enter more than one character, but the program will only read the first character.
user_letter = input("Enter a letter: ")[0]

print("The ASCII equivalent of {} is: {}".format(user_letter, (ord(user_letter))))

# print the following ascii values as characters
# note: this does result in each letter being printed on a new line

ascii_value = [84, 65, 70, 69, 83, 65]

for x in ascii_value:

    print(chr(x))

