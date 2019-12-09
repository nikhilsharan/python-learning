# file input output


print("SANSI")

# input()

ob = open("F:/Classes/Nikhil/python-learning/sample.py", 'r+')

ob.write("""print("hello world")

n = int(input())
written by python r+
""")

print(ob.read(20))

print(ob.tell())

print(ob.seek(10, 0))
ob.close()
