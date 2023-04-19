"""
This program will output the contents of a list using a for loop
"""


# Pseudocode
# OUTPUT HEADING
# cities = ["Adelaide", "Sydney", "Melbourne"]
# FOR index = 1 TO LENGTH(cities)
#   OUTPUT cities[index]
# ENDFOR

def main():
    print("Cities List:")

    cities = ["Adelaide", "Sydney", "Melbourne"]

    for city in cities:
        print(city)


main()
