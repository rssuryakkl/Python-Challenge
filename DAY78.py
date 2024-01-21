#Hii all This is DAY78(21-01-2024) Write a program that finds sum of all even numbers in a list.

num=int(input("Enter a Number:"))
sum=0
i=0
while i<=num:
    if i%2==0:
        print(i)
        sum+=i
    i+=1
print("Sum of all the even number:",sum)
print(f"Sum of all the even number {sum}")
