# Given a string, return a string made of the chars at indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien".

# 0 1 2 3 4 5 6 7 8 9 10
string = input("Enter")
mod_string = ""
counter = 0
limit_list = []
for limit in range(0, string.__len__()):
    if counter == 0:
        counter += 1
        mod_string += string[limit]
        continue
    if counter == 1:
        mod_string += string[limit]
        counter += 1
        continue
    if counter == 2:
        counter += 1
        continue
    if counter == 3:
        counter = 0
        continue

print(mod_string)
