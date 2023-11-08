# take input from user
num = int(input("Enter the number: "))
if num == 1:
    print("{0} is not prime number.".format(num))
elif num > 1:
    # check for factors
    for i in range(2, num):
        if num % i == 0:
            print("{0} is not prime number.".format(num))
            print(i, 'times', num // i, 'is', num)
            break
    else:
        print("{0} is prime number.".format(num))
    # if input number is less than or equal to one
else:
    print("{0} is not prime number.".format(num))