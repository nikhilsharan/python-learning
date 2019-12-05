def sum67(list_elements):
    sum = 0
    for i in range(0,len(list_elements)):
        if list_elements[i] == 6:
            for j in range(list_elements[i+1],len(list_elements)):
                if list_elements[j] == 7:
                    continue
            else:
                sum = sum + list_elements[i]
    return sum
print(sum67([2,3,6,5,3,8,7,1,8]))
