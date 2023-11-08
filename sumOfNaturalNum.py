# sum of natural numbers up to num
num = int(input("Enter the number: "))
sum = 0
# use while loop to iterate until zero
while num > 0:
    sum += num
    num -= 1
print(sum)