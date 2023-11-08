# program to check armstrong number in certain interval
range1 = 100
range2 = 2000
for num in range(range1, range2+1):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if sum == num:
        print(num)