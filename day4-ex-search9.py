# list_element = []

# n = int(input("Enter the limit of the list: "))

# for i in range(0,n):
#     list_element.append(int(input("Enter the elements: ")))

# n = int(input())

list_element = list(input().split(" "))

for i in range(0,len(list_element)):
    list_element[i] = int(list_element[i])
    
for i in range(0,4):
    if list_element[i] == 9:
        print(True)
        break
    else:
        print(False)
        break