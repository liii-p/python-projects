"""
This program will take the length and width of a rectangle then
 calculate the area or the perimeter based on the user's response:
 A (Area) or P (Perimeter)
"""

# pseudocode
# Program rectangle
#   INPUT length
#   INPUT width
#   INPUT choice
#   IF choice = 'A'
#       area = length * width
#       OUTPUT area
#   ELSE if choice = 'P'
#       perimeter = 2 * (length + width)
#       OUTPUT perimeter
#   ENDIF
# END

# input - size of rectangle
length = int(input("Enter the rectangle length: "))
width = int(input("Enter the rectangle width: "))

# input - enter "A" or "P"
choice = input("Enter A for Area or P for Perimeter: ")
choice = choice.upper()
if choice == "A":
    area = length * width
    print("Area is {}".format(area))
elif choice == "P":
    perimeter = 2 * (length + width)
    print("Perimeter is {}".format(perimeter))
