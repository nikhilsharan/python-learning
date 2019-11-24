string = input("Enter the string: ")

new_string = ""

if string[0] == 'I' and string[1] == 's':
    new_string = string
else:
    new_string = "Is" + " " + string
    
print(new_string)

