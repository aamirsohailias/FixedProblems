# find area of triangle
a = int(input("Enter 1st side: "))
b = int(input("Enter 2nd side: "))
c = int(input("Enter 3rd side: "))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
areaOfTriangle = (s * (s-a) * (s-b) * (s-c)) ** 0.5
# display the area of triangle
print("area of triangle is {:0.2f}.".format(areaOfTriangle))