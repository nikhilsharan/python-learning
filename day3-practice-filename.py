# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

filename = input("Enter")

print(filename[1])
flag = 0
extension = ""
for character in filename:
    if character == ".":
        if flag == 1:
            extension = ""
        flag = 1
    if flag == 1:
        extension += character

print(extension)
