list_elem = [3,4,5,7,3245,6,78,5,7,9,0]

n = int(input("Enter the numbeer to be searched"))

ans = False

for x in range(0,len(list_elem)):
    if n == list_elem[x]:
        ans = True
        break
    
print(ans)