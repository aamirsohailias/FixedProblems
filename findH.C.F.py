# using function find the hcf
def compute_hcf(x, y):
    # choose the smaller number
    smaller = min(x, y)
        # find the h. c. f
    for i in range(1, smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf
# take input from user
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
# display the H. C. F
print(f"The H.C.F. of {num1} and {num2} is", compute_hcf(num1, num2),'.')