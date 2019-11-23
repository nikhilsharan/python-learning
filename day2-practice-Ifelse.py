name = input("Enter you name:")

age = int(input("Enter you age:"))

if age >= 18:
	print("You can enter the Pub")
	print("You can have drink as well")

	if age == 75:
		print("Too old to drink")
	elif age == 58 or age == 59:
		print("About to retire")

elif age >= 16 and age < 18:
	print("You can enter the Pub")
	print("Sorry! you cannot have drink, you are too young for it")
	print("Feel free to dance though")

else:
	print("Sorry! you are too young to enter the Pub")