#Hii all This is DAY53(27-12-2023) Today's Topic is Find the number of digits in a number in python
num=int(input("Enter a Number:"))
count=0
while num>0:
    num=num//10
    count=count+1
print("The Number of digits Entered is:",count)
