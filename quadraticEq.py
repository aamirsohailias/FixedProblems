# solve this eq ax**2 + bx + c = 0
a = 5
b = 6
c = 1
# calculate the discriminant
des = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b + (des ** 0.5)) / (2*a)
sol2 = (-b - (des ** 0.5)) / (2*a)
# display the quadratic Eq solution
print("Descriminant: ",des, "\n", "Solutions are {0} and {1}.".format(sol1, sol2))