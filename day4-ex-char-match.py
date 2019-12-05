def stringMatch(name):
    l = len(name)
    if name[0] == name[l-2] and name[1] == name[l-1]:
        return True
    else:
        return False
print(stringMatch(input()))
