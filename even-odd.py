n = int(input())

def isEvenOrOdd(n):
    if n < 0:
        return "Invalid input"
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

ans = isEvenOrOdd(n)

print(ans)