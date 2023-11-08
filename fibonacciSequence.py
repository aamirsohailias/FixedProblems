# take input from user
num = int(input("how many terms?: "))
# first two terms
n1, n2 = 0, 1
# if only one term, return n1
if num == 1:
    print("fibonacci sequence upto nterm", n1)
    # generate fibonacci sequence
else:
    print("fibonacci sequence: ")
    print(n1)
    print(n2)
    # print("fibonacci sequence: ")
    for i in range(4, num+1):
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        print(nth)