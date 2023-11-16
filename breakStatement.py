count = 1
number = int(input('Enter number: '))
while count <= 10:
    result = number * count
    print(number, 'x', count, '=', result)
    if count > 5:
        break
    count += 1