ch = 97
for i in range(0,6):
    for j in range (6,i,-1):
        print(chr(ch), end = '')
        ch += 1
    print()
