# display powers of 2
# taken terms from user
terms = int(input("how many terms?: "))
# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print("total terms are: ", terms)
for i in range(terms):
    # display the powers of two
    print("2 raised to power", i, 'is', result[i])