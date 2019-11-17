from sys import getsizeof

number = 123
floating = 123.123
name = "Abhi"
#
# print(number, name, floating)
#
# print("number " + str(getsizeof(number)))
# print("number " + str(getsizeof(number * 1000)))

number = number1 = 1
print(number, number1)

number, number1, number2, number3 = 1, 1, 2, 3

print(number, number1, number2, number3)

# Standard data types:
#
# Numbers
# Strings
# Lists
# Tuples
# Dictionary

num1 = 1

# del num1

print(num1)

# Three number data types:
# int          float           complex
# 1             0.0              1.1j
# 2            15.15             5+5j
# 3            32.e18
# 0x68

# Strings:

string = "Hello World"

print(string[-5])
print(string[:7])

print(string + string)
print(string * 3)

# Lists:

user_list = ['abc', 1, 5, 12.5, 'Hello']

print(user_list[:3])
print(user_list * 2)
print(user_list + user_list[2:3])
user_list[0] = "List"
print(user_list)

# Tuples

user_tuple = ('abc', 1, 5, 12.5, 'Hello')

print(user_tuple[:3])
print(user_tuple * 2)
print(user_tuple + user_tuple[2:3])
# user_tuple[0] = "List"
print(user_tuple)

# Dictionary:

user_dict = {"key": "value", 1: 4, "password": "Abhi"}
user_dict['food'] = "dosa"

print(user_dict.keys())
print(user_dict.values())
# print(user_dict)

print("List")
print(user_list)
print(list(set(user_list)))

print(int("11", 2))
print(str(11))
# tuple()
# list()
# set()
# dict()
# chr()


print(type("1"))

