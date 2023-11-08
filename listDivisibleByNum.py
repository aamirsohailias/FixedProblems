# nums = int(input("Enter the range: "))
my_list = [12, 65, 54, 39, 102, 339, 221,]
# use anonymous function
result = list(filter(lambda x: x % 13 == 0,my_list))
# display the result
print("numbers divisible by 13 are: ", result)