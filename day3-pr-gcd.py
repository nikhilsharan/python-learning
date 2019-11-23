number1 = int(input("Enter"))
number2 = int(input("Enter"))

gcd = 1

if number1 % number2 == 0:
    gcd = number2
    print(gcd)

for x in range(int(number2/2), 0, -1):
    if number1 % x == 0 and number2 % x == 0:
        gcd = x
        break

print("GCD of ", number1, " and ", number2, " is ", gcd)
