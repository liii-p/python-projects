grade = input("Enter your grade - pass or fail: ")
grade = grade.upper()

result = {"PASS": "Well Done", "FAIL": "Not Good"}

report = result.get(grade, "Incorrect choice entered")

print("The answer is {:s}".format(report))
