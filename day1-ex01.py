# day1-ex01.py
# get user input
# find the data type and print it
# Convert the data type to all other possible data type and print it


myVariable = input("Enter number/word here : ") #always a string so if i want an integer to be my input??
print(type(myVariable))

print(int(myVariable))

print(float(myVariable))

print(set(myVariable))

print(list(myVariable))

print(tuple(myVariable))

# print(chr(myVariable))  #TypeError: an integer is required (got type str)

# print(dict(myVariable))
