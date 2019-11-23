dict_user = {"Name": "A", "Age": 10, "address": "bangalore", "phone": "999", 0: 0, 0: 1}

print(dict_user["Age"])

dict_user["Name"] = "Abhi"

print(dict_user)

del dict_user[0]

print(dict_user)

# dict_user.clear()

# print(dict_user)

print(dict_user.values())
print(dict_user.items())

if "Name" in dict_user:
    print(dict_user["Name"])