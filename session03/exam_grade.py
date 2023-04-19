"""
Program which prints students' grade based on mark %
"""
mark = int(input("Enter your mark (%): "))

if mark < 50:
    print("FL")
elif mark < 65:
    print("PS")
elif mark < 75:
    print("CR")
elif mark < 85:
    print("DN")
else:
    print("HD")
