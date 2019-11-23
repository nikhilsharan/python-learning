n = int(input())
for a in range (2,n+1):

    c = 0
    for i in range (2,a-1):
        if a % i == 0:
            c = 1
            break
#print (c)
    if c == 0:
        print(a, end = " ")
    # else:
    #     print("not prime")
#n = int(input())
