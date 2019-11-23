stringInput = input()

alphabet = 0
consonant = 0
for i in range(0,len(stringInput)):
    if stringInput[i] == 'a' or stringInput[i] == 'e' or stringInput[i] == 'i' or \
    stringInput[i] == 'o' or stringInput[i] == 'u' or stringInput[i] == 'A' or stringInput[i] == 'E' or \
    stringInput[i] == 'I' or stringInput[i] == 'O' or stringInput[i] == 'U':
        alphabet += 1
    else:
        consonant += 1

print("alphabet ", alphabet)
print("consonant ", consonant)
