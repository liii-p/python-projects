# INPUT
# user's name
# user's age
# OUTPUT
# print above input

my_name = input("Enter your first name: ")
my_age = int(input("Enter your age: "))

print("Hello {a}! You are {b} years old.".format(a = my_name, b = my_age))

# age next birthday
print("You will be {b} years old next year.".format(a=my_name, b=(my_age + 1)))

# calculate length of string my_name
print("There are", len(my_name), "characters in your name.")
