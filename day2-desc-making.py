# if:
# Syntax:
# if expression:
#     statements

# if else
# Syntax:
# if expression:
#     statements
# else:
#     statements

# if elif else:
# Syntax:
# if expression:
#     statements
# elif expression:
#     statements
# else:
#     statements

# nested if:
# Syntax:
# if expression:
#   if expression:
#     statements
#   elif expression:
#     statements
#   else:
#     statements
# elif expression:
#     statements
# else:
#     statements


grade = int(input("Enter your grade:"))
print(grade)
if grade < 0 or grade > 100:
    print("Please enter a valid grade")
elif grade < 50:
    print("Failed")
elif grade < 70:
    print("Average")
else:
    if grade > 90:
        print("Excellent")
    else:
        print("Good")
