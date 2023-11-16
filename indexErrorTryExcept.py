try:
    my_list =[1, 2, 3]
    i = int(input("Enter the index: "))
    print(my_list[i])
except IndexError:
    print("index cannot be greater than size of list.")