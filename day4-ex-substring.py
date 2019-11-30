def makeStringOf(out,string_elem):
    return out[0:2] + string_elem + out[2:4]

out = "<<>>"
string_elem = input("Enter the string: ")

print(makeStringOf(out,string_elem))