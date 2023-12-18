#hii all this DAY44(18-12-2023) today's topic is maximum of two numbers
# Python program to find the
# maximum of two numbers


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
a =int(input("Enter a Num1:"))
b =int(input("Enter a Num2:"))
print(maximum(a, b))
