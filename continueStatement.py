count = 0
num = int(input('Enter num: '))
while count < 10:
    count += 1
    result = num * count
    # count += 1
    if count % 2 == 0:
        # print(num, 'x', count, '=', result)
        continue
    print(num, 'x', count, '=', result)