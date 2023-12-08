#hii all this is DAY34(08-12-2023) today's topis is Problems

#Write a program to check if a number is Positive, Negative or zero.
num=int(input("Enter a Number:"))
if (num==0):
    print("Zero")
elif num < 0:
    print("Negative ")
else:
    print("Positive")

#Write a program to display Fibonacci series 
num =10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()















