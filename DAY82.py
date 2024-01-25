#Hii all this is DAY82(25-01-2024) today's Topic is  Write a program that counts the number of times a value appears in the list. Use a loop to do the same.



a = [ ]
n = int(input("Enter number of elements :"))
for i in range(l, n+1):
    b = int(input("Enter element"))
    a.append(b)
    k = 0
    num = int(input("Enter the number to be counted : "))
    for j in a:
        if(j == num):
            k = k+1
        print("Number of times" , num, "appears is", k)
