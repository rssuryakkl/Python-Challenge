#Hii all This is DAY37(11-12-2023) Today's Topic is leap year or not

year=int(input("Enter a year to check leapyear or not:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("Entered Year is Leap Year")
elif(year % 4 ==0) and (year % 100 != 0):
    print("Entered Year is Leap Year")
else:
    print("Not a Leap Year")
