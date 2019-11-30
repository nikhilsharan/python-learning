def firstLast(string_passed,number):
    ans = ""
    for i in range(0,number):
        ans = ans + string_passed[i] 
    for j in range(len(string_passed)-number,len(string_passed)):
        ans = ans + string_passed[j]
    return ans

print(firstLast(input("Enter the string"),int(input("enter number"))))
    
    