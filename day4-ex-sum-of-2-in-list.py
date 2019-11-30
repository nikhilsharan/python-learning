def sumOfTwo(list_elem):
    count = 0
    flag = 0
    for i  in range(0,len(list_elem)):
        if list_elem[i] == 2:
            count = count + list_elem[i]
            if count == 8:
                flag = 1
    #print(count)
    if flag == 1 and count == 8:
        return True    
    else:
        return False

a = [2, 3, 4, 2, 2, 2, 4, 2, 2]

ans = sumOfTwo(a)

print(ans)
