# using function find the lcm
def find_lcm(x, y):
    maxNum = max(x, y)
    # using while statement for iteration
    while True:
        if maxNum % x == 0 and maxNum % y == 0:
            break
        maxNum += 1
        # display the L.C.M of two nums
    print("find the L.C.M of two numbers are: ", maxNum)
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
# call the find_lcm function
find_lcm(num1, num2)