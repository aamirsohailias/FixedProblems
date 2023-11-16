def table_num(num):
    count = 1
    while count < 10:
        result = num * count
        if count > 5:
            break
        print(num, 'x', count, '=', result)
        count += 1
if __name__ == '__main__':
    num = int(input('Enter num: '))
    table_num(num)