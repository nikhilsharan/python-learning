python = "asda"


def binary_search(search_list, to_search):
    new_list = []
    length = search_list.__len__()
    if length == 1:
        print("Element found")
        return
    else:
        if search_list[int(length / 2)] > to_search:
            binary_search(search_list[:int(length / 2)], to_search)
        else:
            binary_search(search_list[int(length / 2):], to_search)


list_sorted = []

for i in range(100):
    list_sorted.append(i)

print(list_sorted)

counter = 0
binary_search(list_sorted, 79)


def prr():
    print(python)
