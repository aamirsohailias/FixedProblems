factorial = 1
# take input from user
num = int(input("Enter the number: "))
i = 1
while i <= num:
    # find the factorial of num
    factorial *= i
    i += 1
# display the factorial
print("The factorial of", num, 'is', factorial)