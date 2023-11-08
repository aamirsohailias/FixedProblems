# taken three input from user
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))
# using if-else statement find the greater number
if num1 > num2 and num1 > num3:
    print("{0} is greater number.".format(num1))
elif num2 > num1 and num2 > num3:
    print("{0} is greater number.".format(num2))
else:
    print("{0} is greater number.".format(num3))

