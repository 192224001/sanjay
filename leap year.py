year=int(input("enter the year"))
if(year%400==0)and(year%100==0):
    print("the year is leap year".format(year))
elif(year%4==0):
    print(" the year is leap year".format(year))
else:
    print("the year is not leap year".format(year))
