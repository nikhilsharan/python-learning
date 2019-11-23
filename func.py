

def exp(x,y):
	result = x**y
	return result

base = int(input("Enter the base:"))
expt = int(input("Enter the exponent:"))

ans = exp(base,expt)

print(ans)

def name(n):
	if n.startswith("n") or n.endswith("h"):
		print("gooffy name")

	else:
		print("swaggy name")

	return n

name_Var = input("Enter a name")

res = name(name_Var)

print (res)