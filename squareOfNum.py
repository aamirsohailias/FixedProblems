# take input from user find square root
num = int(input("enter num: "))
num_square = num ** 0.5
# display the square root of num
print("The square root of %0.1f is %0.2f."%(num, num_square))


# square root of real or complex numbers
# importing complex math module
import cmath
# taken input from user in eval class
num = eval(input("Enter number: "))
num_sqrt = cmath.sqrt(num)
print("The square root of complex num {0} is {1:0.2f} + {2:0.2f}.".format(num, num_sqrt.real,num_sqrt.imag))