print("Calculator\n1.Add")
print("2.Subtract\n3.Multiply\n4.Divide\n5.Exponential\n6.Exit")
option = int(input("Please enter the option for the operation that you want to do:"))

while option != 6:
    if option == 1:
        operand1 = int(input("Enter the first operand"))
        operand2 = int(input("Enter the second operand"))
        print("Addition of " + str(operand1) + " and " + str(operand2) + " = " + str(operand1 + operand2))
    elif option == 2:
        operand1 = int(input("Enter the first operand"))
        operand2 = int(input("Enter the second operand"))
        print("Subtraction of " + str(operand1) + " and " + str(operand2) + " = " + str(operand1 - operand2))
    elif option == 3:
        operand1 = int(input("Enter the first operand"))
        operand2 = int(input("Enter the second operand"))
        print(
            "Multiplication of " + str(operand1) + " and " + str(operand2) + " = " + str(operand1 * operand2))
    elif option == 4:
        operand1 = int(input("Enter the first operand"))
        operand2 = int(input("Enter the second operand"))
        print("Divide of " + str(operand1) + " and " + str(operand2) + " = " + str(operand1 / operand2))
    elif option == 5:
        operand1 = int(input("Enter the first operand"))
        operand2 = int(input("Enter the second operand"))
        print("Exponential of " + str(operand1) + " and " + str(operand2) + " = " + str(operand1 ** operand2))
    print("Calculator\n1.Add")
    print("2.Subtract\n3.Multiply\n4.Divide\n5.Exponential\n6.Exit")
    option = int(input("Please enter the option for the operation that you want to do:"))
print("Thank you for using the Calculator")
