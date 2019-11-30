def areaOfTriangle(base,height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle : "))
height = float(input("Enter the height of triangle : "))

area = areaOfTriangle(base,height)

print(area)

