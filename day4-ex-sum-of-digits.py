def sumOfDigits(digit):
    c = 0
    while digit > 0:
        rem = digit % 10
        c = c + rem
        digit = int(digit / 10)
    return c    
    
        
print(sumOfDigits(int(input("Enter a digit: "))))
        