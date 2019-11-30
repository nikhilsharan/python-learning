def sumOfThree(a,b,c):
    if a == b or a == c or b == c:
        return 0
    else:
        return a+b+c
    
a = int(input("Enter 1st number: "))

b = int(input("Enter 1st number: "))

c = int(input("Enter 1st number: "))

sum = sumOfThree(a,b,c)

print(sum)