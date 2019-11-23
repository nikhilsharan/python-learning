#loops

n = int(input("Enter a number to print its table:"))

for i in range(1,11,2):
	print(n*i)




x = int(input("Enter the 1st num:"))

y = int(input("Enter the 1st num:"))

gcd = 0

for i in range(1,max(x,y)):
	if (x % i == 0 and y % i == 0):
		gcd = i

print (gcd)
print (int((x*y))/gcd)



p = int(input('Enter number for fibonacci series:'))

n1 = 0

n2 = 1

print(n1)

print(n2)

for i in range(2,p+1):
	n = n1 + n2
	print(n)
	n1 = n2
	n2 = n