def sum67(list_elements):
    sum_var = 0
    flag = 0
    for element in list_elements:
        if element == 6:
            flag = 1
        if element == 7:
            flag = 0
            continue
        if flag == 1:
            continue
        else:
            sum_var = sum_var + element
    return sum_var


print(sum67([2, 3, 6, 5, 3, 8, 7, 1, 8]))
