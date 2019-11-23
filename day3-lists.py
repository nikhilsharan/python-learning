list_elements = [1, 2, 3, 4, 5, 6, 7, 1, 2, 43, 5, 5]
tuple_elements = {1, 2, 3, 4, 5, 6, 7}

print(list_elements[5])
print(list_elements[-5:-1])

# list_elements[0] = "1"
print(list_elements)

# list_user = input("Enter the list in space seperated or comma seperated values:").split()
# print(list_user)
# list_for = []
# for i in range(10):
#     list_for.append((input("Enter")))
#
# print(list_for)


print(len(list_elements))
print(list_elements.__len__())
print(list_elements + list_elements)
print(list_elements * 4)

if '5' in list_elements:
    print("yes")

for x in list_elements:
    print(x)

print(list_elements[4:])

print(max(list_elements), min(list_elements))

print(list_elements.count(5))
list_elements.append([1, 2, 3])
list_elements.extend([1, 2, 3])

print(list_elements.index([1, 2, 3]))

print(list_elements.insert(1, 5))
print(list_elements)

list_elements.pop(-4)
print(list_elements)

list_elements.remove(1)
print(list_elements)

print(list_elements.sort())

list_elements_1 = ['a','b','c','e','d']
list_elements_1.sort()
print(list_elements_1)
print(list_elements)

