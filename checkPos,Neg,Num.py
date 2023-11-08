# taken input from user
num = int(input("Enter a number: "))
# implement the deceision making conditions
if num >= 0:
    if num == 0:     # apply the nested if
        print(num, "it is zero.")
    else:
        print(num, "positive num.")
else:
    print(num, "negative num.")
