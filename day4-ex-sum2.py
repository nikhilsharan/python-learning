def sumOfNumbers(a,b):
    if a == b or 15 <= (a+b) <= 20:
        return 20
    else:
        return a+b
    
a = int(input())

b = int(input())

sum = sumOfNumbers(a,b)

print(sum)