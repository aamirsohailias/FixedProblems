# Python program to display all the prime numbers within an interval
lower = int(input("Enter the start range: "))
upper = int(input("Enter the end range: "))
print("prime numbers between", lower, 'and', upper, 'are: ')
for num in range(lower, upper+1):
    # all prime numbers greater than 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)