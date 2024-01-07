#Hii all This is DAY64(07-01-2024) Today's topics is simple MCQ's  Write a program to swap two values using tuple assignment

list = [2**x for x in range(5)]
print(list)

#Write a program to swap two values using tuple assignment
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
print("Value of A = ", a, "\n Value of B = ", b)
(a, b) = (b, a)
print("Value of A = ", a, "\n Value of B = ", b)
