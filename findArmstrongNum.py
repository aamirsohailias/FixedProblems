# take input from user
num = int(input("Enter the number: "))
order = len(str(num))
sum = 0
# find the sum of cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
    # display the result
if sum == num:
    print('{0} is an armstrong number.'.format(num))
else:
    print('{0} is not armstrong number.'.format(num))

