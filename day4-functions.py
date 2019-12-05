from datetime import date

def name(n, b="s"):
    """This is the documention
    This is for the function"""
    print("This is the " + n + b)
    return print("Hi")


print(name("Abhi"))
print(name.__doc__)


def variable_sum(a, b, *variable):
    sum_var = 0
    sum_var = a + b
    print(type(variable))
    for i in variable:
        sum_var += i
    print("Sum is ", sum_var)
    return


variable_sum(1, 5)

variable_sum(1, 4, 5, 6, 7, 8)

addition = lambda var1, var2: var1 + var2

print(addition(1, 2))

