for i in range(1,6):
    for j in range(1,i+1):
        if j % 2 == 0:
            continue
        print(j,end = '')
    print()
