num = int(input("Enter the number: "))
counter = 1
# using while statement
while counter <= 10:
    product =  num * counter
    # display the multiplication table
    print(num, '*', counter, '=', product)
    counter += 1