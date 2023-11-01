# take input from user
kilo_meter = eval(input("Enter kilo meter which you are travelling: "))
# conversion factor
one_kilo = 0.621371
# calculate miles
miles = kilo_meter*one_kilo
# display the miles
print("%0.2f kilometers is equal to %0.2f miles." % (kilo_meter, miles))