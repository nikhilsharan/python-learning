def swapFirstLast(list_elem):
    x = list_elem[0]
    l = len(list_elem)
    list_elem[0] = list_elem[l-1]
    list_elem[l-1] = x
    return list_elem

a = [2, 4, 6, 8, 9, 10]

print(swapFirstLast(a))