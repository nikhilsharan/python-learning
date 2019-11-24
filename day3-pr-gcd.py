number1 = int(input("Enter"))
number2 = int(input("Enter"))

gcd = 0

# if number1 % number2 == 0:
#     gcd = number2
#     print(gcd)

for x in range(1,number1+1 and number2+1):
    if number1 % x == 0 and number2 % x == 0:
        gcd = x
        

print("GCD of ", number1, " and ", number2, " is ", gcd)
